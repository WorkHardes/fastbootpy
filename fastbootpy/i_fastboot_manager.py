import abc


class IFastbootManager(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def devices() -> list[str]:
        raise NotImplementedError
