from __future__ import annotations
from typing import List, Any
from copy import deepcopy


class Queue:

    def __init__(self) -> None:
        self.__dados: List[Any] = []
        self.__index = 0

    def enqueue(self, elemento: Any) -> None:
        self.__dados.insert(0, elemento)

    def dequeue(self) -> Any:
        return self.__dados.pop()

    def peek(self) -> Any:
        if not self.__dados:
            return []
        return self.__dados[-1]

    def __iter__(self) -> Queue:
        self.__index = len(self.__dados)
        return self

    def __next__(self) -> Any:
        if self.__index == 0:
            raise StopIteration
        self.__index -= 1
        return self.__dados[self.__index]

    def __bool__(self) -> bool:
        return bool(self.__dados)

    def __repr__(self) -> str:
        return f"{self.__dados}"