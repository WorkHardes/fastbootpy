from fastbootpy.fastboot_protocol import FastbootProtocol


def main() -> None:
    prefix = "getvar"
    arg = "all"
    encoded_cmd = FastbootProtocol.encode_cmd(prefix, arg)
    print("encoded_cmd:", encoded_cmd)


if __name__ == "__main__":
    main()
