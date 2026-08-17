from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """Reorder L0→L1→…→Ln as L0→Ln→L1→Ln−1→… in place.

        Three steps: slow/fast split at the middle, reverse the back half,
        then interleave the two halves stitch by stitch. O(n) time, O(1) space.
        """
        if not head or not head.next:
            return
        # 1. split
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        back = slow.next
        slow.next = None
        # 2. reverse back half
        prev = None
        while back:
            back.next, prev, back = prev, back, back.next
        # 3. interleave
        a, b = head, prev
        while b:
            a.next, b.next, a, b = b, a.next, a.next, b.next


if __name__ == "__main__":
    def build(vals):
        h = ListNode(vals[0]); c = h
        for v in vals[1:]:
            c.next = ListNode(v); c = c.next
        return h
    h = build([1, 2, 3, 4, 5])
    Solution().reorderList(h)
    got = []
    while h:
        got.append(h.val); h = h.next
    assert got == [1, 5, 2, 4, 3], got
    print("ok")
