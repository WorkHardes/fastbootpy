import os
import unittest

from fastbootpy import FastbootDevice, USBError


FASTBOOT_DEVICE_SERIAL = os.getenv("FASTBOOT_DEVICE_SERIAL")


class TestFastbootDevice(unittest.TestCase):
    def test_connect(self):
        try:
            FastbootDevice.connect(FASTBOOT_DEVICE_SERIAL)
            return False
        except USBError:
            return True


if __name__ == "__main__":
    unittest.main()
