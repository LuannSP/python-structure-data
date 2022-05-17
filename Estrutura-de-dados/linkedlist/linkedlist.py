from multiprocessing.sharedctypes import Value
from operator import index
from node import Node


class LinkedList:

    def __init__(self):
        self.head = None
        self.__size = 0

    def append(self, elem):
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            self.head = Node(elem)
        self.__size += 1

    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")

    def __setitem__(self, index, elem):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
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
        raise ValueError(f"{i} is not in list")

    def __len__(self):
        return self.__size


list = LinkedList()

list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)

# print(len(list))

#a = list[4]

# print(a)

#list[4] = 10

#a = list[4]

# print(a)

# print(list.index(5))
