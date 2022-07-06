from typing import Any


class TreeNode:

    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.left: TreeNode = None
        self.right: TreeNode = None

    def __str__(self) -> str:
        return str(self.data)
