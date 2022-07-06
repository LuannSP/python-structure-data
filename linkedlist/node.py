from typing import Any


class Node:

    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self._next: Node = None
