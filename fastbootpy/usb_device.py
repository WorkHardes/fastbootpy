from __future__ import annotations

import usb

import exceptions
import i_usb_device


class USBDevice(i_usb_device.IUSBDevice):
    def __init__(
        self,
        usb_device: usb.core.Device,
        read_endpoint: usb.core.Endpoint,
        write_endpoint: usb.core.Endpoint,
        read_timeout: int,
        write_timeout: int,
    ) -> None:
        self.usb_device = usb_device
        self.read_endpoint = read_endpoint
        self.write_endpoint = write_endpoint
        self.read_timeout = read_timeout
        self.write_timeout = write_timeout

    def send(self, data: bytes) -> None:
        try:
            self.write_endpoint.write(data, self.write_timeout)
        except usb.USBError:
            raise exceptions.USBError()

    def recv(self) -> bytes:
        device_response = b""
        buffer = b""
        while True:
            try:
                buffer = self.read_endpoint.read(
                    4096,
                    self.read_timeout,
                )
            except usb.USBError:
                break

            if buffer == None or buffer == b"":
                break
            else:
                device_response += buffer

        return device_response

    def flush_buffer(self) -> None:
        while True:
            try:
                buffer = self.read_endpoint.read(
                    4096,
                    self.read_timeout,
                )
            except usb.USBError:
                break

            if buffer == None or buffer == b"":
                break

    @staticmethod
    def _get_r_w_endpoints(
        usb_device: usb.core.Device,
    ) -> tuple[usb.core.Endpoint | None, usb.core.Endpoint | None]:
        write_endpoint, read_endpoint = None, None
        for cfg in usb_device:
            for iface in cfg:
                for endpoint in iface:
                    if (
                        usb.core.util.endpoint_direction(endpoint.bEndpointAddress)
                        == usb.core.util.ENDPOINT_IN
                    ):
                        read_endpoint = endpoint
                    else:
                        write_endpoint = endpoint
        return read_endpoint, write_endpoint

    @staticmethod
    def _get_usb_device(serial: str) -> usb.core.Device | None:
        for device in usb.core.find(find_all=True):
            try:
                if device.serial_number == serial:
                    return device
            except ValueError:
                pass
        return None

    @classmethod
    def get_fastboot_device(
        cls,
        serial: str,
        read_timeout: int,
        write_timeout: int,
    ) -> USBDevice:
        usb_device = cls._get_usb_device(serial)
        if usb_device is None:
            raise exceptions.USBError()

        try:
            usb_device.reset()
        except Exception:
            raise exceptions.USBError()

        if usb_device.is_kernel_driver_active(0):
            usb_device.detach_kernel_driver(0)

        read_endpoint, write_endpoint = cls._get_r_w_endpoints(usb_device)
        if write_endpoint is None or read_endpoint is None:
            raise exceptions.USBError()

        return cls(
            usb_device, read_endpoint, write_endpoint, read_timeout, write_timeout
        )
