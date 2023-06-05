import re
import shlex

from ..command import Command
from ..correct import Correct
from ..registry import registry
from ..utils import fast_filter


@fast_filter("git", "push")
def git_push(command: Command):
    match = re.search(
        r"fatal: The current branch (?P<branch>.*?) has no upstream branch.",
        command.stderr.decode(),
    )
    if match:
        return Correct(
            shlex.split(f"git push --set-upstream origin {match.group('branch')}")
        )


registry(git_push)
