import os
import unittest

from fastbootpy import FastbootDevice


FASTBOOT_DEVICE_SERIAL = os.getenv("FASTBOOT_DEVICE_SERIAL")
if FASTBOOT_DEVICE_SERIAL is None:
    FASTBOOT_DEVICE_SERIAL = "emulator-5554"

device = FastbootDevice.connect(FASTBOOT_DEVICE_SERIAL)


class FastbootDeviceTest(unittest.TestCase):
    def test_send(self):
        self.assertEqual(device.send(b"hello:hello"), "FAILunknown command")

    def test_getvar(self):
        self.assertEqual(
            device.getvar("serialno"),
            f"OKAY{FASTBOOT_DEVICE_SERIAL}",
        )


if __name__ == "__main__":
    unittest.main()
