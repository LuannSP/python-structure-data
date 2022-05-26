from tree_node import TreeNode
from queue import Queue


ROOT = "root"


class TreeBinary():

    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = TreeNode(data)
            self.root = node
        else:
            self.root = None

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node, end=' ')
        if node.right:
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node, end='')

    def height(self, node=None):
        if node is None:
            node = self.root
        h_left = 0
        h_right = 0
        if node.left:
            h_left = self.height(node.left)
        if node.right:
            h_right = self.height(node.right)
        if h_left > h_right:
            return h_left + 1
        return h_right + 1

    def levelorder_traversal(self, node=ROOT):
        if node == ROOT:
            node = self.root
        queue = Queue()
        queue.enqueue(node)
        while len(queue):
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
            print(node, end=" ")
