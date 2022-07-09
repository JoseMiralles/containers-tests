from typing import Generic, Optional, TypeVar, List

T = TypeVar("T")

class Node(Generic[T]):
    def __init__(self, _value: T):
        self._value: T = _value
        self._parent: "Optional[Node[T]]" = None
        self._children: "List[Node[T]]" = []

    @property
    def value(self) -> T:
        return self._value

    @property
    def children(self) -> "List[Node[T]]":
        return self._children

    @property
    def parent(self) -> "Optional[Node[T]]":
        return self._parent

    @parent.setter
    def parent(self, _parent: "Optional[Node[T]]") -> None:
        if self._parent:
            self._parent.children.remove(self)
        self._parent = _parent
        if (self._parent):
            self._parent.children.append(self)

    def add_child(self, child: "Node[T]") -> None:
        self._children.append(child)
        child._parent = self

    def remove_child(self, child: "Node[T]") -> None:
        try: self._children.remove(child)
        except: pass
        finally:
            if (child.parent):
                child.parent = None

    def __repr__(self) -> str:
        return f"<Node object {self._value}>"
        