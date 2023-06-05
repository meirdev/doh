import difflib
import os
import re

from ..command import Command
from ..correct import Correct
from ..registry import registry
from ..utils import fast_filter

THRESHOLD = 0.85


def strcmp(a: str, b: str) -> float:
    return difflib.SequenceMatcher(a=a, b=b).ratio()


@fast_filter("cat")
def cat(command: Command):
    match = re.search(
        r"cat: (?P<filename>.*?): No such file or directory",
        command.stderr.decode(),
    )
    if match:
        err_filename = match.group("filename")

        for filename in os.listdir():
            if strcmp(filename, err_filename) >= THRESHOLD:
                return Correct(["cat", filename])


registry(cat)
