import os
import unittest

from fastbootpy.exceptions import USBError
from fastbootpy.fastboot_device import FastbootDevice


FASTBOOT_DEVICE_SERIAL = os.getenv("FASTBOOT_DEVICE_SERIAL")

device = FastbootDevice().connect(FASTBOOT_DEVICE_SERIAL)


class FastbootDeviceTest(unittest.TestCase):
    def test_send(self):
        self.assertEqual(device.send(b"hello:hello"), "FAILunknown command")

    def test_getvar(self):
        self.assertEqual(
            device.getvar("serialno"),
            f"OKAY{FASTBOOT_DEVICE_SERIAL}",
        )

    def test_reboot_bootloader(self):
        try:
            device.reboot_bootloader()
            return False
        except USBError:
            return True


if __name__ == "__main__":
    unittest.main()
