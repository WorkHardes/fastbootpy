import abc


class IFastbootProtocol(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def encode_cmd(prefix: str, arg: str | None = None) -> bytes:
        raise NotImplementedError
