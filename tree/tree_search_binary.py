from tree_binary import TreeBinary
from tree_node import TreeNode
from typing import Any
from __future__ import annotations

ROOT: str = "root"


class TreeSearchBinary(TreeBinary):

    def insert(self, elem: Any) -> None:
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

    def search(self, elem: Any) -> (TreeSearchBinary | Any | None):
        return self._search(elem, self.root)

    def _search(self, elem: Any, node: TreeNode) -> (TreeSearchBinary | Any | None):
        if node is None:
            return None
        if node.data == elem:
            return TreeSearchBinary(node)
        if elem < node.data:
            return self._search(elem, node.left)
        return self._search(elem, node.right)

    def min(self, node: str | TreeNode = ROOT) -> (Any | None):
        if node == ROOT:
            if self.root is None:
                return None
            node = self.root
        while node.left:
            node = node.left
        return node.data

    def max(self, node: str | TreeNode = ROOT) -> (Any | None):
        if node == ROOT:
            if self.root is None:
                return None
            node = self.root
        while node.right:
            node = node.right
        return node.data

    def remove(self, elem: Any, node: str | TreeNode = ROOT) -> (Any | None):
        if node == ROOT:
            node = self.root
        if node is None:
            return node
        if elem < node.data:
            node.left = self.remove(elem, node.left)
        elif elem > node.data:
            node.right = self.remove(elem, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                substitute = self.min(node.right)
                node.data = substitute
                node.right = self.remove(substitute, node.right)
        return None
