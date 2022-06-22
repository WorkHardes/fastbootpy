import abc


class IFastbootManager(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def devices() -> list[str]:
        """Returns list of fastboot device serial numbers."""
        raise NotImplementedError
