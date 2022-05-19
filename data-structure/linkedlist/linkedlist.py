from multiprocessing.sharedctypes import Value
from operator import index, truediv
from node import Node


class LinkedList:

    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            self.head = Node(elem)
        self._size += 1

    def __getitem__(self, index):
        pointer = self._getNode(index)
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")

    def __setitem__(self, index, elem):
        pointer = self._getNode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")

    def index(self, elem):
        i = 0
        pointer = self.head
        while pointer:
            if pointer.data == elem:
                return i
            else:
                pointer = pointer.next
                i += 1
        raise ValueError(f"{elem} is not in list")

    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getNode(index-1)
            node.next = pointer.next
            pointer.next = node
        self._size += 1

    def remove(self, elem):
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

    def _getNode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer

    def __repr__(self):
        list = []
        pointer = self.head
        while pointer:
            list.append(pointer.data)
            pointer = pointer.next
        return str(list)

    def __len__(self):
        return self._size


"""

from linkedlist import LinkedList

list = LinkedList()

list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)

print(list)

"""
