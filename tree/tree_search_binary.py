from tree_binary import TreeBinary
from tree_node import TreeNode


class TreeSearchBinary(TreeBinary):

    def insert(self, elem):
        parent = None
        aux = self.root
        while aux:
            parent = aux
            if elem < aux.data:
                aux = aux.left
            else:
                aux = aux.right
        if parent is None:
            self.root = TreeNode(elem)
        elif elem < parent.data:
            parent.left = TreeNode(elem)
        else:
            parent.right = TreeNode(elem)

    def search(self, elem):
        return self._search(elem, self.root)

    def _search(self, elem, node):
        if node is None:
            return None
        if node.data == elem:
            return TreeSearchBinary(node)
        if elem < node.data:
            return self._search(elem, node.left)
        return self._search(elem, node.right)


# def search(self, elem, node=0):
#     if node == 0:
#         node = self.root
#     if node is None or node.data == elem:
#         return TreeSearchBinary(node)
#     if elem < node.data:
#         return self.search(elem, node.left)
#     return self.search(elem, node.right)

# arvore = TreeSearchBinary()

# random.seed(77)
# dados = random.sample(range(1, 1000), 100)
# procurados = [1, 1000, 510, 188, 866]

# for r in dados:
#     arvore.insert(r)

# arvore.inorder_traversal()

# for procurado in procurados:
#     node = arvore.search(procurado)
#     if node is None:
#         print('\n', procurado, 'nao encontrado')
#     else:
#         print('\n', procurado, 'econtrado')
