import argparse

from .logger import logger
from .main import run


def main() -> None:
    arg_parser = argparse.ArgumentParser("D'oh!")
    arg_parser.add_argument("command")
    arg_parser.add_argument("--output", default=None)

    args = arg_parser.parse_args()

    command = args.command.strip()
    output = args.output

    logger.debug("User command: %s", command)

    if output:
        with open(output, "rb") as fp:
            output = fp.read()

    try:
        run(command, output)
    except Exception as exc:
        logger.debug(str(exc))
        exit(1)


if __name__ == "__main__":
    main()
