from typing import Optional


class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None


class LRUCache:
    """Least-recently-used cache with O(1) get and put.

    A hash map (key → node) plus a doubly linked list in recency order:
    the head side is most recent, the tail side least. get/put move a
    node to the head; overflow evicts the tail — all O(1) because the
    list is doubly linked.
    """

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map: dict[int, Node] = {}
        self.head = Node(0, 0)  # dummy most-recent
        self.tail = Node(0, 0)  # dummy least-recent
        self.head.next, self.tail.prev = self.tail, self.head

    def _unlink(self, node: Node) -> None:
        node.prev.next, node.next.prev = node.next, node.prev

    def _push_front(self, node: Node) -> None:
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._unlink(node)
        self._push_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._unlink(self.map[key])
        node = Node(key, value)
        self.map[key] = node
        self._push_front(node)
        if len(self.map) > self.cap:
            lru = self.tail.prev
            self._unlink(lru)
            del self.map[lru.key]


if __name__ == "__main__":
    c = LRUCache(2)
    c.put(1, 1); c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)                      # evicts 2
    assert c.get(2) == -1
    c.put(4, 4); assert c.get(1) == -1
    assert c.get(3) == 3 and c.get(4) == 4
    print("ok")
