import abc
from abc import ABC
from typing import List, Tuple

from elenchos.nagios.NagiosStatus import NagiosStatus
from elenchos.nagios.PerformanceData import PerformanceData


class NagiosPlugin(ABC):
    """
    Abstract parent class for Nagios plugins.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, name: str):
        """
        Object constructor.

        :param str name: The name of this Nagios plugin.
        """
        self._name: str = name
        """
        The name of this Nagios plugin.
        """

        self.__performance_data: List[PerformanceData] = []
        """
        The list of performance data of this Nagios plugin.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def __check_performance_data(self) -> Tuple[NagiosStatus, List[str], List[str]]:
        """
        Aggregates the list of performance data and returns the worst status, a list of performance descriptions to be
        included in the description of the Nagios check, and a list of formatted performance data.
        """
        status = NagiosStatus.OK
        header_list = []
        performance_list = []
        for performance_data in self.__performance_data:
            if performance_data.include_in_description():
                header_list.append(performance_data.header())
            performance_list.append(performance_data.performance())
            status = status.worst(performance_data.check())

        return status, header_list, performance_list

    # ------------------------------------------------------------------------------------------------------------------
    def _add_performance_data(self, performance_data: PerformanceData) -> None:
        """
        Adds performance data to this Nagios plugin.

        :param PerformanceData performance_data: The performance data.
        """
        self.__performance_data.append(performance_data)

    # ------------------------------------------------------------------------------------------------------------------
    def _get_description(self, status: NagiosStatus, header_list: List[str]) -> str:
        """
        Returns the description of the check of this Nagios plugin.

        :param NagiosStatus status: The status of the check of this Nagios plugin.
        :param List[str] header_list: The list of headers of the performance data.

        :rtype: str
        """
        return ', '.join(header_list)

    # ------------------------------------------------------------------------------------------------------------------
    def _get_performance(self, status: NagiosStatus, performance_list: List[str]) -> str:
        """
        Returns the description of the check of this Nagios plugin.

        :param NagiosStatus status: The status of the check of this Nagios plugin.
        :param List[str] performance_list: The list of the performance data.

        :rtype: str
        """
        return ' '.join(performance_list)

    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def _self_check(self) -> NagiosStatus:
        """
        This method must be implemented by concrete instances to perform the actual check of this Nagios plugin. This
        method may use method _add_performance_data() for adding performance data to this Nagios elenchos.

        :rtype: NagiosStatus
        """
        raise NotImplementedError()

    # ------------------------------------------------------------------------------------------------------------------
    def check(self) -> NagiosStatus:
        """
        Executes the actual check of this Nagios plugin and does all administration for return status, message, and
        performance data.

        :rtype: NagiosStatus
        """
        status_self = self._self_check()
        status_perf, header_list, performance_list = self.__check_performance_data()
        status = status_self.worst(status_perf)

        message = "{} {}".format(self._name, status.name)
        description = self._get_description(status, header_list)
        performance = self._get_performance(status, performance_list)
        if description:
            message += ": " + description
        if performance:
            message += " | " + performance

        print('{}\n'.format(message.strip()))

        return status

# ----------------------------------------------------------------------------------------------------------------------
