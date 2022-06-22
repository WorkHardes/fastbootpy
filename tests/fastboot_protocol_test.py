import unittest

from fastbootpy import FastbootProtocol


class TestFastbootProtocol(unittest.TestCase):
    def test_encode_cmd1(self) -> None:
        prefix = "getvar"
        arg = "all"
        rigth_emcoded_cmd1 = b"getvar:all"
        self.assertEqual(FastbootProtocol.encode_cmd(prefix, arg), rigth_emcoded_cmd1)

    def test_encode_cmd2(self) -> None:
        prefix = "reboot"
        arg = None
        rigth_emcoded_cmd2 = b"reboot"
        self.assertEqual(FastbootProtocol.encode_cmd(prefix, arg), rigth_emcoded_cmd2)

    def test_encode_cmd3(self) -> None:
        prefix = "reboot-bootloader"
        rigth_emcoded_cmd3 = b"reboot-bootloader"
        self.assertEqual(FastbootProtocol.encode_cmd(prefix), rigth_emcoded_cmd3)

    def test_encode_cmd4(self) -> None:
        prefix = "None"
        arg = "flash"
        rigth_emcoded_cmd4 = b"None:flash"
        self.assertEqual(FastbootProtocol.encode_cmd(prefix, arg), rigth_emcoded_cmd4)

    def test_encode_cmd5(self) -> None:
        prefix = "None"
        arg = "None"
        rigth_emcoded_cmd5 = b"None:None"
        self.assertEqual(FastbootProtocol.encode_cmd(prefix, arg), rigth_emcoded_cmd5)


if __name__ == "__main__":
    unittest.main()
