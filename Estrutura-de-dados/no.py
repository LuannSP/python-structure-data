class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2.data
n2.next = n3.data
n3.next = n4.data
n4.next = n5.data

print(n1.data)
print(n1.next)
print(n2.next)
print(n3.next)
print(n4.next)
