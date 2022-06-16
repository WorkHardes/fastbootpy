from __future__ import annotations
import abc

import usb


class IUSBDevice(abc.ABC):
    def send(self, data: bytes) -> None:
        raise NotImplementedError

    def recv(self) -> bytes:
        raise NotImplementedError

    def flush_buffer(self) -> None:
        raise NotImplementedError

    @staticmethod
    def _get_r_w_endpoints(
        usb_device: usb.core.Device,
    ) -> tuple[usb.core.Endpoint | None, usb.core.Endpoint | None]:
        raise NotImplementedError

    @staticmethod
    def _get_usb_device(serial: str) -> usb.core.Device | None:
        raise NotImplementedError

    @classmethod
    def get_fastboot_device(
        cls,
        serial: str,
        read_timeout: int,
        write_timeout: int,
    ) -> IUSBDevice:
        raise NotImplementedError
