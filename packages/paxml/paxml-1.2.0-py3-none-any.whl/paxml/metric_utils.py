# coding=utf-8
# Copyright 2022 The Pax Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Utility functions for metric evaluation in Pax."""

import numbers
import typing
from typing import Any, Mapping, Sequence, Tuple

from absl import logging
import clu.metrics as clu_metrics
import clu.values as clu_values
import jax
from jax import numpy as jnp
import numpy as np
from paxml import summary_utils
# Internal platform import
from praxis import py_utils
from praxis import pytypes
import seqio
from tensorflow.compat.v2 import summary as tf_summary

# internal runtime import


Metrics = pytypes.Metrics
WeightedScalar = pytypes.WeightedScalar
WeightedScalars = pytypes.WeightedScalars
WeightedScalarsList = pytypes.WeightedScalarsList

NestedMap = py_utils.NestedMap
SummaryValueTypes = (
    clu_values.Scalar
    | clu_values.Image
    | clu_values.Text
    | clu_values.Summary
    | clu_values.Histogram
    | clu_values.Audio
)


_VALUES_TO_SUMMARY_TYPE = {
    clu_values.Scalar: summary_utils.SummaryType.SCALAR,
    clu_values.Text: summary_utils.SummaryType.TEXT,
    clu_values.Image: summary_utils.SummaryType.IMAGE,
    # Videos (GIFs) are written to tensorboard as clu.values.summary.
    clu_values.Summary: summary_utils.SummaryType.VIDEO,
    clu_values.Histogram: summary_utils.SummaryType.HISTOGRAM,
    clu_values.Audio: summary_utils.SummaryType.AUDIO,
}


def _get_summary_type(
    metric_value: SummaryValueTypes,
) -> summary_utils.SummaryType:
  """Infers metric summary type from the metric value type."""
  if type(metric_value) not in _VALUES_TO_SUMMARY_TYPE:
    raise ValueError(f'Unknown metric value type: {type(metric_value)}.')
  return _VALUES_TO_SUMMARY_TYPE[type(metric_value)]


def compute_metric_values(metrics: Metrics) -> dict[str, SummaryValueTypes]:
  """Given a dict of clu_metrics.Metric objects, returns their values.

  Args:
    metrics: A dict[str, clu_metrics.Metric] objects with a compute_value()
      function implemented that returns either a clu_values.Value object, a
      dict[str, clu_values.Value] objects, a dict[str, List[clu_values.Value]]
      objects, or a List[clu_values.Value].

  Returns:
    metric_values: A flattened dict[str, clu_values.Value] objects.
  """
  logging.info('Computing metric values.')
  metric_values = {}
  for metric_name, metric in metrics.items():
    logging.info('Computing metric %s', metric_name)
    metric_value = metric.compute_value()
    # compute_value can return either a scalar clu_values.Value object,
    # a dict[str, clu_values.Value] objects, a dict[str, List[clu_values.Value]]
    # objects, or a List[clu_values.Value] objects.
    if isinstance(metric_value, dict):
      for key, value in metric_value.items():
        summary_key = f'{metric_name}/{key}'
        if isinstance(value, (list, tuple)):
          for i, subval in enumerate(value):
            summary_key_i = f'{summary_key}_{i}'
            metric_values[summary_key_i] = subval
        else:
          metric_values[summary_key] = value
    elif isinstance(metric_value, (list, tuple)):
      for i, value in enumerate(metric_value):
        metric_values[f'{metric_name}/{metric_name}_{i}'] = value
    elif isinstance(
        metric_value,
        (
            clu_values.Scalar,
            clu_values.Image,
            clu_values.Text,
            clu_values.Histogram,
            clu_values.Audio,
        ),
    ):
      metric_values[f'{metric_name}'] = metric_value
    else:
      raise ValueError(
          'Unrecognized compute_value() output format for metric '
          f'{metric_name}: {type(metric_value)}.'
      )
  return metric_values


def write_clu_metric_summaries(
    metric_values: dict[str, SummaryValueTypes], step_i: int
) -> None:
  """Given a dict of metric values, writes them out as tensorboard summaries.

  This is expected to be called under a summary context.

  Args:
    metric_values: A dict[str, Any] objects with metric values. These values are
      one of the various clu_values.Value subtypes.
    step_i: An int representing the current step of decoding.
  """
  if not metric_values:
    return

  logging.info('Summarizing metrics.')
  for metric_name, metric_value in metric_values.items():
    logging.info('Summarizing metric %s', metric_name)
    summary_type = _get_summary_type(metric_value)
    # Pass both value and metadata to write_summary_tensor for video summary.
    if isinstance(metric_value, clu_values.Summary):
      summary_utils.write_summary_tensor(
          step_i,
          metric_name,
          metric_value.value,
          summary_type,
          metric_value.metadata,
      )
    elif isinstance(metric_value, clu_values.Audio):
      summary_utils.write_summary_tensor(
          step_i,
          metric_name,
          metric_value.value,
          summary_type,
          sample_rate=metric_value.sample_rate,
      )
    else:
      summary_utils.write_summary_tensor(
          step_i, metric_name, metric_value.value, summary_type
      )


def compute_and_write_clu_metric_summaries(metrics: Metrics, step: int) -> None:
  """Compute clu_metrics.Metric objects values and write them out as summaries.

  Args:
    metrics: A Dict[str, clu_metrics.Metric] objects with a compute_value()
      function implemented that returns either a clu_values.Value object, a
      Dict[str, clu_values.Value] objects, a Dict[str, List[clu_values.Value]]
      objects, or a List[clu_values.Value].
    step: An int representing the current step of decoding.
  """
  if metrics:
    # Convert metrics to Dict[str, clu_values.Value] for summary writing.
    clu_metric_values = compute_metric_values(metrics)
    write_clu_metric_summaries(clu_metric_values, step)


def write_seqio_metric_summaries(
    seqio_metrics: Sequence[Mapping[str, seqio.metrics.MetricValue | float]],
    metric_name_prefix: str,
    step: int,
) -> None:
  """Write seqio metric as tensorboard summaries.

  Args:
    seqio_metrics: A sequence of dict of str to seqio metric value or float.
    metric_name_prefix: A prefix added to metric name.
    step: An int. representing the current step.
  """
  for m_dict in seqio_metrics:
    for k, v in m_dict.items():
      metric_name = f'{metric_name_prefix}/{k}'
      if isinstance(v, seqio.metrics.Text):
        metric_str = (
            v.textdata.decode() if isinstance(v.textdata, bytes) else v.textdata
        )
        logging.info(
            'Writing summary of %s with string value %s.',
            metric_name,
            metric_str,
        )
        tf_summary.text(metric_name, metric_str, step=step)
        continue

      if isinstance(v, seqio.metrics.Audio):
        logging.info('Writing summary of %s with audio.', metric_name)
        tf_summary.audio(
            metric_name,
            v.audiodata,
            v.sample_rate,
            step=step,
            max_outputs=v.max_outputs,
        )
        continue

      if isinstance(v, seqio.metrics.Image):
        logging.info('Writing summary of %s with image.', metric_name)
        tf_summary.image(
            metric_name,
            v.image,
            step=step,
            max_outputs=v.max_outputs)
        continue

      if isinstance(v, seqio.metrics.Histogram):
        tf_summary.histogram(metric_name, v.values, buckets=v.bins, step=step)
        continue

      if isinstance(v, seqio.metrics.Generic):
        tf_summary.write(metric_name, v.tensor, metadata=v.metadata, step=step)
        continue

      if isinstance(v, seqio.metrics.Scalar):
        v = float(v.value)
      else:
        v = float(v)
      logging.info('Writing summary of %s with value %.4f.', metric_name, v)
      summary_utils.write_summary_tensor(
          step, metric_name, v, summary_utils.SummaryType.AGGREGATE_SCALAR
      )


def is_scalar(v: Any) -> bool:
  """Returns True if input is a scalar."""
  scalar_types = [
      numbers.Number,
      np.ndarray,
      jnp.ndarray,
      jax.Array,
  ]
  # Internal scalar types
  return isinstance(v, tuple(scalar_types))


def is_weighted_scalar(v: Any) -> bool:
  """Returns True if input is a weighted scalar."""
  return (
      isinstance(v, tuple)
      and len(v) == 2
      and is_scalar(v[0])
      and is_scalar(v[1])
  )


def is_float_convertible(
    metric_value: numbers.Number | clu_values.Value | seqio.metrics.MetricValue,
):
  """Returns True if a metricv value is float convertible."""
  return (
      isinstance(metric_value, numbers.Number)
      or isinstance(metric_value, clu_values.Scalar)
      or isinstance(metric_value, seqio.metrics.Scalar)
      or is_weighted_scalar(metric_value)
      or (
          isinstance(metric_value, list)
          and all(is_weighted_scalar(v) for v in metric_value)
      )
  )


def as_float(
    metric_value: numbers.Number
    | clu_values.Scalar
    | seqio.metrics.Scalar
    | WeightedScalar
    | Sequence[WeightedScalar],
) -> float:
  """Returns the aggregated float value from heterogeneous metric value."""
  if is_weighted_scalar(metric_value):
    metric_value = [metric_value]

  if isinstance(metric_value, list):
    assert all(is_weighted_scalar(v) for v in metric_value), metric_value
    values = np.stack([x[0] for x in metric_value])
    weights = np.stack([x[1] for x in metric_value])
    return np.sum(values * weights) / np.sum(weights)
  if isinstance(metric_value, (clu_values.Scalar, seqio.metrics.Scalar)):
    return metric_value.value  # pytype: disable=bad-return-type  # numpy-scalars
  assert isinstance(metric_value, numbers.Number), metric_value
  return float(typing.cast(Any, metric_value))


def as_float_dict(
    metric_output: dict[str, SummaryValueTypes]
    | WeightedScalars
    | WeightedScalarsList
    | Mapping[str, seqio.metrics.MetricValue | float],
    raise_on_non_float_convertible: bool = False,
) -> dict[str, float]:
  """Returns a float dict from heterogeneous metric output."""
  results = {}
  for k, v in metric_output.items():
    if not is_float_convertible(v):
      if raise_on_non_float_convertible:
        raise ValueError(f'Summary value cannot be converted to float: {v}.')
      continue
    results[k] = as_float(v)
  return results


def update_float_dict(
    target: dict[str, float],
    source: dict[str, float],
    prefix: str | None = None,
) -> dict[str, float]:
  """Inserts items from source dict to target dict with an optional prefix."""
  if prefix is None:
    target.update(source)
  else:
    for k, v in source.items():
      target[f'{prefix}/{k}'] = v
  return target


def merge_clu_metrics(metrics: Metrics, updated_metrics: Metrics) -> Metrics:
  """Merges updated metric data with existing metrics."""
  if metrics:
    if set(metrics.keys()) != set(updated_metrics.keys()):
      raise ValueError(
          'metrics and updated_metrics keys don`t match. '
          f'metrics keys: {metrics.keys()} '
          f'updated_metrics keys: {updated_metrics.keys()}'
      )

    for key in metrics:
      metrics[key] = metrics[key].merge(updated_metrics[key])
  else:
    metrics = updated_metrics
  return metrics


def extract_weighted_scalars_and_clu_metrics(
    metrics: dict[str, Any]
) -> Tuple[WeightedScalars, Metrics]:
  """Extracts weighted scalars and clu metrics from metrics dict.

  Args:
    metrics: Metrics data output by the model.

  Returns:
    A tuple of weighted scalars or clu.metrics. Only one of these will be
    returned by the model in its outputs, so one of the
    tuple elements will be an empty dictionary.
  """
  if isinstance(metrics, NestedMap):
    metric_values = metrics.Flatten()
  else:
    metric_values = metrics.values()

  for metric_value in metric_values:
    if is_weighted_scalar(metric_value):
      return metrics, {}
    elif isinstance(metric_value, clu_metrics.Metric):
      return {}, metrics
    else:
      raise TypeError(
          '`metrics` must be a `WeightedScalars` or `clu.Metrics`. Instead its'
          ' type is %s.'
          % type(metrics)
      )
  raise TypeError(
      '`metrics` must be a `WeightedScalars` or `clu.Metrics`. Instead its'
      ' type is %s.'
      % type(metrics)
  )
