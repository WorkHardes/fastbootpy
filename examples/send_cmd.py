from fastbootpy.fastboot_device import FastbootDevice


def main() -> None:
    serial = "emulator-5554"
    device = FastbootDevice().connect(serial)
    result = device.send("getvar:unlocked")
    print("result:", result)


if __name__ == "__main__":
    main()
