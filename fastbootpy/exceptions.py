__all__ = [
    "CommonUSBException",
    "USBError",
    "DeviceNotFoundError",
]


class CommonUSBException(Exception):
    def __init__(self) -> None:
        self.message = "Device connection error."

    def __str__(self) -> str:
        return self.message

    def __repr__(self) -> str:
        return self.message


class USBError(CommonUSBException):
    def __init__(self, serial: str, exception: Exception | None = None) -> None:
        self.message = f"Device '{serial}' connection error."
        if exception is not None:
            self.message += f"Detail: {repr(exception)}"


class DeviceNotFoundError(CommonUSBException):
    def __init__(self, serial) -> None:
        self.message = f"Device '{serial}' not found."
