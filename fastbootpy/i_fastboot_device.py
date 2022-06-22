from __future__ import annotations
import abc

from fastbootpy import fastboot_manager


class IFastbootDevice(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def connect(
        serial: str,
        read_timeout: int = fastboot_manager.DERAULT_USB_READ_TIMEOUT,
        write_timeout: int = fastboot_manager.DERAULT_USB_WRITE_TIMEOUT,
    ) -> IFastbootDevice:
        """Returns FastbootDevice class instance.

        Raises:
            exceptions.DeviceNotFoundError: if device not found
            exceptions.USBError: if excepted usb.USBError or TimeoutError
        """
        raise NotImplementedError

    @abc.abstractmethod
    def send(self, cmd: str | bytes) -> str:
        """Sends command on device and returns it result.

        Args:
            cmd (str | bytes): fastboot command

        Raises:
            usb.USBError: if excepted usb.usb.USBError or TimeoutError

        Returns:
            str: result of inputed command
        """
        raise NotImplementedError

    @abc.abstractmethod
    def getvar(self, variable: str) -> str:
        """Inputs getvar command and returns it result."""
        raise NotImplementedError

    @abc.abstractmethod
    def download(self, data: bytes) -> None:
        """Inputs download command."""
        raise NotImplementedError

    @abc.abstractmethod
    def upload(self) -> None:
        """Inputs upload command."""
        raise NotImplementedError

    @abc.abstractmethod
    def flash(self, partition: str) -> None:
        """Inputs flash command."""
        raise NotImplementedError

    @abc.abstractmethod
    def erase(self, partition: str) -> None:
        """Inputs erase command."""
        raise NotImplementedError

    @abc.abstractmethod
    def boot(self) -> None:
        """Inputs boot command."""
        raise NotImplementedError

    @abc.abstractmethod
    def continue_(self) -> None:
        """Inputs continue command."""
        raise NotImplementedError

    @abc.abstractmethod
    def reboot(self, mode: str | None = None) -> None:
        """Reboot device in inputed mode."""
        raise NotImplementedError

    @abc.abstractmethod
    def reboot_bootloader(self) -> None:
        """Reboot device into bootloader."""
        raise NotImplementedError
