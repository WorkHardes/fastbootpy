from fastbootpy.fastboot_manager import FastbootManager


def main() -> None:
    fastboot_devices = FastbootManager.devices()
    print("fastboot_devices:", fastboot_devices)


if __name__ == "__main__":
    main()
