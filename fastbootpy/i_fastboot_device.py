from __future__ import annotations
import abc

import usb


DEFAULT_TIMEOUT = 10000


class IFastbootDevice(abc.ABC):
    @property
    def usb_handle(self) -> usb.core.Device:
        raise NotImplementedError

    def open(self) -> None:
        raise NotImplementedError

    def close(self) -> None:
        raise NotImplementedError

    def connect(self, serial: str, timeout: int = DEFAULT_TIMEOUT) -> IFastbootDevice:
        raise NotImplementedError

    def send(self, cmd: str | bytes) -> str:
        raise NotImplementedError

    def getvar(self, variable: str) -> str:
        raise NotImplementedError

    def download(self, data: bytes) -> None:
        raise NotImplementedError

    def upload(self) -> None:
        raise NotImplementedError

    def flash(self, partition: str) -> None:
        raise NotImplementedError

    def erase(self, partition: str) -> None:
        raise NotImplementedError

    def boot(self) -> None:
        raise NotImplementedError

    def continue_fastboot(self) -> None:
        raise NotImplementedError

    def reboot(self, mode: str | None = None) -> None:
        raise NotImplementedError

    def reboot_bootloader(self) -> None:
        raise NotImplementedError
