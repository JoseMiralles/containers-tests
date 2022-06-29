from typing import (
    Generic,
    Optional,
    TypeVar,
    List,
    Tuple)

T = TypeVar("T")

class TreeNodeIterator(Generic[T]):
    """
    Handles iterating over tree
    """
    def __init__(self, _tree_node: "TreeNode[T]") -> None:
        self._root: "TreeNode[T]" = _tree_node
        self._index: int = 0
        self._qu: "List[TreeNode[T]]" = [self._root]

    def __next__(self) -> Tuple[T, int]:
        if not self._qu: raise StopIteration
        _current = self._qu.pop()
        self._index += 1
        if _current.left: self._qu.append(_current.left)
        if _current.right: self._qu.append(_current.right)
        return (_current.value, self._index)

class TreeNode(Generic[T]):

    left: "Optional[TreeNode[T]]" = None
    right: "Optional[TreeNode[T]]" = None

    def __init__(self, value: T) -> None:
        super().__init__()
        self._value = value

    def __iter__(self) -> TreeNodeIterator[T]:
        return TreeNodeIterator(self)

    @property
    def value(self) -> T:
        return self._value

root: TreeNode[int] = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

for val, i in root:
    print(f"Value: {val}, Index: {i}")
