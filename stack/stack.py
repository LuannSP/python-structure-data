from __future__ import annotations
from typing import Any, List


class Stack:

    def __init__(self) -> None:
        self._data: List[Any] = []
        self._index: int = 0
        self._size: int = 0

    def push(self, elem: Any) -> None:
        self._data.append(elem)
        self._size += 1

    def pop(self) -> Any:
        if not self._size:
            raise IndexError("the stack is empty")
        self._size -= 1
        return self._data.pop()

    def peek(self) -> Any:
        if not self._data:
            return []
        return self._data[-1]

    def __iter__(self) -> Stack:
        self._index = len(self._data)
        return self

    def __next__(self) -> Any:
        if self._index == 0:
            raise StopIteration
        self._index -= 1
        return self._data[self._index]

    def __bool__(self) -> bool:
        return bool(self._data)

    def __repr__(self) -> str:
        return f"{self._data}"

    def __len__(self) -> int:
        return self._size
