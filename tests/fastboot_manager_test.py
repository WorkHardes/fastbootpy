import os

import unittest

from fastbootpy.fastboot_manager import FastbootManager


FASTBOOT_DEVICE_SERIAL = os.getenv("FASTBOOT_DEVICE_SERIAL")
fastboot_devices = [FASTBOOT_DEVICE_SERIAL]


class TestFastbootManager(unittest.TestCase):
    def test_devices(self):
        self.assertEqual(FastbootManager.devices(), fastboot_devices)


if __name__ == "__main__":
    unittest.main()
