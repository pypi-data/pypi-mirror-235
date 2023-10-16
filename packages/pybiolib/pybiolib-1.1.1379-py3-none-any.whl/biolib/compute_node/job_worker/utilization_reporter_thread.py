import threading
import time
import subprocess
from datetime import datetime

import docker.errors  # type: ignore
from docker.models.containers import Container  # type: ignore

import biolib.api.client
from biolib.biolib_logging import logger_no_user_data
from biolib.typing_utils import List, TypedDict, Optional, Dict, cast


class UtilizationMetricSample(TypedDict):
    cpu_usage_in_percent: float
    gpu_usage_in_percent: Optional[float]
    memory_usage_in_percent: float


class AggregatedUtilizationMetrics(TypedDict):
    cpu_average_usage_in_percent: float
    cpu_max_usage_in_percent: float
    gpu_average_usage_in_percent: Optional[float]
    gpu_max_usage_in_percent: Optional[float]
    memory_average_usage_in_percent: float
    memory_max_usage_in_percent: float
    recorded_at: str
    sampling_period_in_milliseconds: int


class UtilizationReporterThread(threading.Thread):
    def __init__(self, container: Container, job_uuid: str, compute_node_auth_token: str):
        super().__init__(daemon=True)
        self._container_object: Container = container
        self._job_uuid: str = job_uuid
        self._compute_node_auth_token: str = compute_node_auth_token

        self._sampling_period_in_milliseconds = 1_000
        self._samples_between_writes = 60

    def run(self) -> None:
        logger_no_user_data.debug(f'Job "{self._job_uuid}" utilization metrics reporter thread started')
        prev_cpu_usage: Optional[float] = None
        prev_cpu_system_usage: Optional[float] = None
        metric_samples: List[UtilizationMetricSample] = []
        while True:
            stats = self._get_container_stats()
            if not stats:
                break

            if prev_cpu_usage is None or prev_cpu_system_usage is None:
                prev_cpu_usage = stats['cpu_stats']['cpu_usage']['total_usage']
                prev_cpu_system_usage = stats['cpu_stats']['system_cpu_usage']
                continue

            # Calculate CPU usage
            cpu_usage_delta_ns = stats['cpu_stats']['cpu_usage']['total_usage'] - prev_cpu_usage
            cpu_system_usage_delta_ns = stats['cpu_stats']['system_cpu_usage'] - prev_cpu_system_usage
            cpu_usage_in_percent = round((cpu_usage_delta_ns / cpu_system_usage_delta_ns) * 100, ndigits=2)

            # Set previous usage
            prev_cpu_usage = stats['cpu_stats']['cpu_usage']['total_usage']
            prev_cpu_system_usage = stats['cpu_stats']['system_cpu_usage']

            # Calculate Memory usage
            memory_usage_in_percent = round(
                stats['memory_stats']['usage'] / stats['memory_stats']['limit'] * 100,
                ndigits=2,
            )

            metric_samples.append(UtilizationMetricSample(
                cpu_usage_in_percent=cpu_usage_in_percent,
                memory_usage_in_percent=memory_usage_in_percent,
                gpu_usage_in_percent=self._get_gpu_utilization_in_percent(),
            ))

            if len(metric_samples) >= self._samples_between_writes:
                self._report_aggregated_utilization_metric(metric_samples)
                metric_samples = []

            time.sleep(secs=self._sampling_period_in_milliseconds / 1_000)

        # Write the remaining samples after container has exited
        self._report_aggregated_utilization_metric(metric_samples)
        logger_no_user_data.debug(f'Job "{self._job_uuid}" utilization metrics reporter thread exiting')

    @staticmethod
    def _get_gpu_utilization_in_percent() -> Optional[float]:
        try:
            cmd = 'nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader'
            utilization = subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL).decode('utf-8')
            utilization_for_each_gpu = [float(x.replace(' %', '')) for x in utilization.strip().split('\n')]
            utilization_for_first_gpu = utilization_for_each_gpu[0]
            return utilization_for_first_gpu
        except BaseException as error:
            logger_no_user_data.exception(f'Failed to get GPU utilization got error: {error}')
            return None

    def _get_container_stats(self) -> Optional[Dict]:
        try:
            return cast(Dict, self._container_object.stats(stream=False))
        except docker.errors.NotFound:
            return None

    def _get_aggregated_utilization_metric_from_metric_samples(
            self,
            metric_samples: List[UtilizationMetricSample],
    ) -> AggregatedUtilizationMetrics:
        cpu_max_usage_in_percent: float = 0.0
        cpu_usage_in_percent_sum: float = 0.0
        gpu_max_usage_in_percent: Optional[float] = None
        gpu_usage_in_percent_sum: Optional[float] = None
        memory_max_usage_in_percent: float = 0.0
        memory_usage_in_percent_sum: float = 0.0

        for metric_sample in metric_samples:
            cpu_max_usage_in_percent = max(cpu_max_usage_in_percent, metric_sample['cpu_usage_in_percent'])
            cpu_usage_in_percent_sum += metric_sample['cpu_usage_in_percent']
            memory_max_usage_in_percent = max(memory_max_usage_in_percent, metric_sample['memory_usage_in_percent'])
            memory_usage_in_percent_sum += metric_sample['memory_usage_in_percent']

            if metric_sample['gpu_usage_in_percent'] is not None:
                if gpu_max_usage_in_percent is None:
                    gpu_max_usage_in_percent = 0.0
                if gpu_usage_in_percent_sum is None:
                    gpu_usage_in_percent_sum = 0.0

                gpu_max_usage_in_percent = max(gpu_max_usage_in_percent, metric_sample['gpu_usage_in_percent'])
                gpu_usage_in_percent_sum += metric_sample['gpu_usage_in_percent']

        cpu_average_usage_in_percent = cpu_usage_in_percent_sum / len(metric_samples)
        memory_average_usage_in_percent = memory_usage_in_percent_sum / len(metric_samples)
        gpu_average_usage_in_percent = gpu_usage_in_percent_sum / len(metric_samples) \
            if gpu_usage_in_percent_sum is not None else None

        return AggregatedUtilizationMetrics(
            cpu_average_usage_in_percent=cpu_average_usage_in_percent,
            cpu_max_usage_in_percent=cpu_max_usage_in_percent,
            gpu_average_usage_in_percent=gpu_average_usage_in_percent,
            gpu_max_usage_in_percent=gpu_max_usage_in_percent,
            memory_average_usage_in_percent=memory_average_usage_in_percent,
            memory_max_usage_in_percent=memory_max_usage_in_percent,
            recorded_at=datetime.utcnow().isoformat(),
            sampling_period_in_milliseconds=self._sampling_period_in_milliseconds * self._samples_between_writes,
        )

    def _report_aggregated_utilization_metric(self, metric_samples: List[UtilizationMetricSample]) -> None:
        if len(metric_samples) == 0:
            logger_no_user_data.debug(f'Job "{self._job_uuid}" no metric samples to aggregate. Skipping reporting.')
            return

        aggregated_metrics = self._get_aggregated_utilization_metric_from_metric_samples(metric_samples)
        logger_no_user_data.debug(f'Job "{self._job_uuid}" reporting aggregated metrics {aggregated_metrics}')

        response = biolib.api.client.post(
            path=f'/internal/compute-nodes/jobs/{self._job_uuid}/utilization-metrics/',
            headers={'Compute-Node-Auth-Token': self._compute_node_auth_token},
            data=cast(Dict, aggregated_metrics),
        )

        if not response.ok:
            logger_no_user_data.error(
                f'Failed to report metrics got status {response.status_code} and error: {response.text}'
            )
