import typing
from dataclasses import dataclass

from netmeasure.measurements.base.results import MeasurementResult
from netmeasure.units import TimeUnit, StorageUnit, RatioUnit, NetworkUnit


@dataclass(frozen=True)
class SpeedtestDotnetMeasurementResult(MeasurementResult):
    """Encapsulates the results from a speedtest_dotnet measurement.

    :param download_rate: The measured download rate.
    :param download_rate_unit: The unit of measurement of `download_rate`.
    :param upload_rate: The measured upload rate.
    :param upload_rate_unit: The unit of measurement of `upload_rate`.
    :param data_received: The quantity of data received by the speedtest utility
    :param data_received_unit: The unit of measurement of `data_received`
    :param data_sent: The quantity of data sent by the speedtest utility
    :param data_sent_unit: The unit of measurement of `data_received`
    :param latency: The measured latency.
    :param server_name: The name of the speedtest.net server used to perform
    the speedtest_dotnet measurement.
    :param server_id: The id of the speedtest.net server used to perform the
    speedtest_dotnet measurement.
    :param server_sponsor: The sponsor of the speedtest.net server used to
    perform the speedtest_dotnet measurement.
    :param server_host: The host name of the speedtest.net server used to
    perform the speedtest_dotnet measurement.
    """

    download_rate: typing.Optional[float]
    download_rate_unit: typing.Optional[NetworkUnit]
    upload_rate: typing.Optional[float]
    upload_rate_unit: typing.Optional[NetworkUnit]
    data_received: typing.Optional[float]
    data_received_unit: typing.Optional[StorageUnit]
    data_sent: typing.Optional[float]
    data_sent_unit: typing.Optional[StorageUnit]
    latency: typing.Optional[float]
    server_name: typing.Optional[str]
    server_id: typing.Optional[str]
    server_sponsor: typing.Optional[str]
    server_host: typing.Optional[str]
