# Fastbootpy

Fastbootpy is based on pyusb and using libusb1 for USB communications.

---

## Installation

### pip

```bash
poetry add fastbootpy
```

### poetry

```bash
poetry add fastbootpy
```

---

## Examples

All examples of using library you can find in folder examples.

Get and display all fastboot devices which are connected with pc via usb.

```python
from fastbootpy import FastbootManager


def main() -> None:
    fastboot_devices = FastbootManager.devices()
    print("fastboot_devices:", fastboot_devices)


if __name__ == "__main__":
    main()
```

Boot device into regular mode.

```python
from fastbootpy import FastbootDevice


def main() -> None:
    serial = "emulator-5554"
    device = FastbootDevice.connect(serial)
    device.boot()


if __name__ == "__main__":
    main()
```

Getvar command example.

```python
from fastbootpy import FastbootDevice, FastbootManager


def main() -> None:
    fastboot_devices = FastbootManager.devices()
    serial = fastboot_devices[0]
    device = FastbootDevice.connect(serial)
    result = device.getvar("all")
    print("result:", result)


if __name__ == "__main__":
    main()

```
