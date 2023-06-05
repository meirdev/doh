from typing import Iterator

from .rule import Rule


class Registry:
    def __init__(self) -> None:
        self._registry: list[Rule] = []

    def __call__(self, rule: Rule) -> None:
        self._registry.append(rule)

    def __iter__(self) -> Iterator[Rule]:
        yield from self._registry


registry = Registry()
