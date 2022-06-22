from __future__ import annotations
import abc

import usb


class IUSBDevice(abc.ABC):
    @abc.abstractmethod
    def send(self, data: bytes) -> None:
        """Sends bytes on device via USB."""
        raise NotImplementedError

    @abc.abstractmethod
    def recv(self) -> bytes:
        """Receives all data via USB."""
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def _get_r_w_endpoints(
        usb_device: usb.core.Device,
    ) -> tuple[usb.core.Endpoint | None, usb.core.Endpoint | None]:
        """Returns read and write endpoints of USB interface."""
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def _get_pyusb_device(serial: str) -> usb.core.Device | None:
        """Returns puysb(usb.core.Device) instance."""
        raise NotImplementedError

    @abc.abstractmethod
    def _flush_buffer(self) -> None:
        """Read all data from read endpoint."""
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def get_usb_device(
        cls,
        serial: str,
        read_timeout: int,
        write_timeout: int,
    ) -> IUSBDevice:
        """Returns USBDevice instance.

        Raises:
            exceptions.DeviceNotFoundError: if device not found
            exceptions.USBError: if excepted usb.USBError or TimeoutError
        """
        raise NotImplementedError
