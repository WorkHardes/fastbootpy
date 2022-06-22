from fastbootpy import FastbootDevice


def main() -> None:
    serial = "emulator-5554"
    device = FastbootDevice.connect(serial)
    device.boot()


if __name__ == "__main__":
    main()
