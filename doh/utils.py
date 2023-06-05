from functools import wraps
from typing import Callable, Optional

from .command import Command
from .correct import Correct
from .rule import Rule


def fast_filter(*args: str) -> Callable[[Rule], Rule]:
    def inner(fn: Rule) -> Rule:
        @wraps(fn)
        def wrapper(command: Command) -> Optional[Correct | list[Correct]]:
            cmd_args = iter(command.args)

            if not all(next(cmd_args, None) == i for i in args):
                return None

            return fn(command)

        return wrapper

    return inner
