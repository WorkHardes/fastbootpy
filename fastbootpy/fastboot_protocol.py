from fastbootpy import i_fastboot_protocol


ENCODING = "utf-8"


class FastbootProtocol(i_fastboot_protocol.IFastbootProtocol):
    @staticmethod
    def encode_cmd(prefix: str, arg: str | None = None) -> bytes:
        if arg is None:
            return prefix.encode(ENCODING)
        return f"{prefix}:{arg}".encode(ENCODING)
