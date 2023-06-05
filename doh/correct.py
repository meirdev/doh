from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Correct:
    args: list[str]
    side_effect: Callable[[], None] | None = None
    weight: float = 1.0
