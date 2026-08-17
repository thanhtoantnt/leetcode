from typing import Optional


class Node:
    def __init__(self, x: int, next: "Optional[Node]" = None, random: "Optional[Node]" = None):
        self.val = x
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """Deep-copy a list whose nodes also carry a random pointer.

        Three passes: (1) interleave a clone after every original node;
        (2) each clone's random = its original's random's successor
        (which is that target's clone); (3) unzip into two lists.
        O(n) time, O(1) extra space. The map-free twin of the
        hash-map solution (old -> clone dict) used in 0133 clone-graph.
        """
        if not head:
            return None
        cur = head
        while cur:  # 1. interleave clones
            clone = Node(cur.val, cur.next)
            cur.next = clone
            cur = clone.next
        cur = head
        while cur:  # 2. wire randoms
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        cur = head
        clone_head = head.next
        while cur:  # 3. unzip
            clone = cur.next
            cur.next = clone.next
            if clone.next:
                clone.next = clone.next.next
            cur = cur.next
        return clone_head


if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    a.next, b.next = b, None
    a.random, b.random = b, a
    c = Solution().copyRandomList(a)
    assert c.val == 1 and c.random.val == 2 and c.next.random.val == 1 and c.next is not b
    print("ok")
