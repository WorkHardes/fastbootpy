from __future__ import annotations

from fastbootpy import fastboot_protocol
from fastbootpy import usb_device
from fastbootpy import i_fastboot_device


DERAULT_WRITE_TIMEOUT = 100
DERAULT_READ_TIMEOUT = 100


class FastbootDevice(i_fastboot_device.IFastbootDevice):
    def __init__(self):
        self._usb_handle = None
        self.serial = None

    def connect(
        self,
        serial: str,
        read_timeout: int = DERAULT_READ_TIMEOUT,
        write_timeout: int = DERAULT_WRITE_TIMEOUT,
    ) -> FastbootDevice:
        self.serial = serial
        self._usb_handle = usb_device.USBDevice.get_fastboot_device(
            serial, read_timeout, write_timeout
        )
        return self

    def send(self, cmd: str | bytes) -> str:
        if isinstance(cmd, str):
            encoded_cmd = cmd.encode("utf-8")
        else:
            encoded_cmd = cmd

        self._usb_handle.send(encoded_cmd)
        device_response = self._usb_handle.recv()
        return device_response.decode("utf-8")

    def getvar(self, variable: str) -> str:
        prefix = "getvar"
        cmd = fastboot_protocol.FastbootProtocol.encode_cmd(prefix, variable)
        return self.send(cmd)

    def download(self, data: bytes) -> None:
        prefix = "download"
        cmd = fastboot_protocol.FastbootProtocol.encode_cmd(prefix, data)
        self.send(cmd)

    def upload(self) -> None:
        prefix = "upload"
        cmd = fastboot_protocol.FastbootProtocol.encode_cmd(prefix)
        self.send(cmd)

    def flash(self, partition: str) -> None:
        prefix = "flash"
        cmd = fastboot_protocol.FastbootProtocol.encode_cmd(prefix, partition)
        self.send(cmd)

    def erase(self, partition: str) -> None:
        prefix = "erase"
        cmd = fastboot_protocol.FastbootProtocol.encode_cmd(prefix, partition)
        self.send(cmd)

    def boot(self) -> None:
        prefix = "boot"
        cmd = fastboot_protocol.FastbootProtocol.encode_cmd(prefix)
        self.send(cmd)

    def continue_(self) -> None:
        prefix = "continue"
        cmd = fastboot_protocol.FastbootProtocol.encode_cmd(prefix)
        self.send(cmd)

    def reboot(self, mode: str | None = None) -> None:
        prefix = "reboot"
        cmd = fastboot_protocol.FastbootProtocol.encode_cmd(prefix, mode)
        self.send(cmd)

    def reboot_bootloader(self) -> None:
        prefix = "reboot-bootloader"
        cmd = fastboot_protocol.FastbootProtocol.encode_cmd(prefix)
        self.send(cmd)
