import abc


class IFastbootProtocol(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def encode_cmd(prefix: str, arg: str | None = None) -> bytes:
        """Returns an encoded command using the fastboot protocol."""
        raise NotImplementedError
