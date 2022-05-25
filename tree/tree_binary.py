from tree_node import TreeNode


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


# if __name__ == "__main__":

#     tree = TreeBinary()

#     n1 = TreeNode('L')
#     n2 = TreeNode('U')
#     n3 = TreeNode('A')
#     n4 = TreeNode('N')
#     n5 = TreeNode('N')

#     n6 = TreeNode('N')
#     n7 = TreeNode('N')
#     n8 = TreeNode('N')

#     tree.root = n8

#     n5.left = n3
#     n5.right = n4
#     n3.left = n1
#     n3.right = n2

#     n4.left = n6
#     n4.right = n7
#     n7.right = n8

#     tree.postorder_traversal()

#     print(tree.height())

    # n1 = TreeNode(1)
    # n2 = TreeNode(2)
    # n3 = TreeNode(3)
    # n4 = TreeNode(4)
    # n5 = TreeNode(5)

    # tree.root = n1

    # n1.left = n2
    # n1.right = n3

    # n3.left = n4
    # n3.right = n5

    # tree.inoder()

    # n1 = TreeNode('a')
    # n2 = TreeNode('+')
    # n3 = TreeNode('*')
    # n4 = TreeNode('b')
    # n5 = TreeNode('-')
    # n6 = TreeNode('/')
    # n7 = TreeNode('c')
    # n8 = TreeNode('d')
    # n9 = TreeNode('e')

    # n6.left = n7
    # n6.right = n8
    # n5.left = n6
    # n5.right = n9
    # n3.left = n4
    # n3.right = n5
    # n2.left = n1
    # n2.right = n3

    # tree.root = n2

    # tree.inoder()
