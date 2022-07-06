from __future__ import annotations
from typing import Any, List


class Queue:

    def __init__(self) -> None:
        self._dados: List[Any] = []
        self._index: int = 0
        self._size: int = 0

    def enqueue(self, elem: Any) -> None:
        self._dados.insert(0, elem)
        self._size += 1

    def dequeue(self) -> Any:
        if self._size:
            self._size -= 1
            return self._dados.pop()
        raise IndexError("the queue is empty")

    def peek(self) -> Any:
        if not self._dados:
            return []
        return self._dados[-1]

    def __iter__(self) -> Queue:
        self._index = len(self._dados)
        return self

    def __next__(self) -> Any:
        if self._index == 0:
            raise StopIteration
        self._index -= 1
        return self._dados[self._index]

    def __bool__(self) -> bool:
        return bool(self._dados)

    def __repr__(self) -> str:
        return f"{self._dados}"

    def __len__(self) -> int:
        return self._size
