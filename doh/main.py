import shlex
import subprocess

from .command import Command
from .correct import Correct
from .logger import logger
from .registry import registry
from .ui import select_command


class NoCorrectsFound(Exception):
    pass


class UserCanceled(Exception):
    pass


def find_possible_corrects(command: Command) -> list[Correct]:
    commands: set[tuple[str, ...]] = set()
    corrects: list[Correct] = []

    for rule in registry:
        result = rule(command)
        if result is None:
            continue

        if isinstance(result, Correct):
            result = [result]

        for correct in result:
            args = tuple(correct.args)
            if args not in commands:
                commands.add(args)
                corrects.append(correct)

    return sorted(corrects, key=lambda x: x.weight, reverse=True)


def run(command: str, output: bytes | None = None) -> None:
    command_args = shlex.split(command)

    if output is None:
        proc = subprocess.run(command, shell=True, capture_output=True)

        cmd = Command(
            command_args,
            stdout=proc.stdout,
            stderr=proc.stderr,
            exit_code=proc.returncode,
        )
    else:
        cmd = Command(
            command_args,
            stdout=b"",
            stderr=output,
            exit_code=0,
        )

    corrects = find_possible_corrects(cmd)
    if len(corrects) == 0:
        raise NoCorrectsFound

    correct_commnads = [shlex.join(correct.args) for correct in corrects]

    logger.debug("Correct commands: %s", correct_commnads)

    idx = select_command(correct_commnads)
    if idx is None:
        raise UserCanceled

    selected_correct = corrects[idx]
    command = correct_commnads[idx]

    logger.debug("Selected command: %s", command)

    if selected_correct.side_effect:
        selected_correct.side_effect()

    subprocess.run(command, shell=True)
