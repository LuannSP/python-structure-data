class Queue:

    def __init__(self):
        self._dados = []
        self._index = 0
        self._size = 0

    def enqueue(self, elem):
        self._dados.insert(0, elem)
        self._size += 1

    def dequeue(self):
        if self._size:
            self._size -= 1
            return self._dados.pop()
        raise IndexError("the queue is empty")

    def peek(self):
        if not self._dados:
            return []
        return self._dados[-1]

    def __iter__(self):
        self._index = len(self._dados)
        return self

    def __next__(self):
        if self._index == 0:
            raise StopIteration
        self._index -= 1
        return self._dados[self._index]

    def __bool__(self):
        return bool(self._dados)

    def __repr__(self):
        return f"{self._dados}"

    def __len__(self):
        return self._size
