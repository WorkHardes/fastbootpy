import usb

from fastbootpy import i_fastboot_manager


FASTBOOT_CLASS = 0xFF
FASTBOOT_SUBCLASS = 0x42
FASTBOOT_PROTOCOL = 0x03

DERAULT_USB_READ_TIMEOUT = 500
DERAULT_USB_WRITE_TIMEOUT = 500


class FastbootManager(i_fastboot_manager.IFastbootManager):
    @staticmethod
    def devices() -> list[str]:
        fastboot_devices: list[str] = []
        for device in usb.core.find(find_all=True):
            for cfg in device:
                dev = usb.util.find_descriptor(
                    cfg,
                    bInterfaceClass=FASTBOOT_CLASS,
                    bInterfaceSubClass=FASTBOOT_SUBCLASS,
                    bInterfaceProtocol=FASTBOOT_PROTOCOL,
                )
                if dev is None:
                    continue
                else:
                    try:
                        fastboot_devices.append(device.serial_number)
                    except (usb.USBError, ValueError):
                        pass
        return fastboot_devices
