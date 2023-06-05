from typing import Callable, Optional

from .command import Command
from .correct import Correct

Rule = Callable[[Command], Optional[Correct | list[Correct]]]
