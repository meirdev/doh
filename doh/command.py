from dataclasses import dataclass


@dataclass(frozen=True)
class Command:
    args: list[str]
    stdout: bytes
    stderr: bytes
    exit_code: int
