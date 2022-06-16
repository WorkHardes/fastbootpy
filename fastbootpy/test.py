import fastboot_device


if __name__ == "__main__":
    serial = "3cd482340106"
    dev = fastboot_device.FastbootDevice().connect(serial)
    result = dev.getvar("unlocked")
    print("result:", result)
