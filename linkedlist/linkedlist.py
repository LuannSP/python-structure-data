from typing import Any
from node import Node


class LinkedList:

    def __init__(self) -> None:
        self.head: Any = None
        self._size: int = 0

    def append(self, elem: Any) -> None:
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            self.head = Node(elem)
        self._size += 1

    def __getitem__(self, index: int) -> Any:
        pointer = self._getNode(index)
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")

    def __setitem__(self, index: int, elem: Any) -> None:
        pointer = self._getNode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")

    def index(self, elem: Any) -> int:
        i = 0
        pointer = self.head
        while pointer:
            if pointer.data == elem:
                return i
            else:
                pointer = pointer.next
                i += 1
        raise ValueError(f"{elem} is not in list")

    def insert(self, index: int, elem: Any) -> None:
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getNode(index-1)
            node.next = pointer.next
            pointer.next = node
        self._size += 1

    def remove(self, elem: Any) -> bool:
        if self.head == None:
            raise ValueError(f"{elem} is not in list")
        elif self.head.data == elem:
            self.head = self.head.next
            self._size -= 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while pointer:
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                    self._size -= 1
                    return True
                ancestor = pointer
                pointer = pointer.next
        raise ValueError(f"{elem} is not in list")

    def _getNode(self, index: int) -> None:
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer

    def __repr__(self) -> str:
        list = ""
        pointer = self.head
        while pointer:
            list += (f"{pointer.data} -> ")
            pointer = pointer.next
        return list

    def __len__(self) -> int:
        return self._size
