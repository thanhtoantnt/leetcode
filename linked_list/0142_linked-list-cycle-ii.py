from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Return the node where the cycle begins (or None).

        Floyd's, phase 2 (0141's flipbook derived it): after the
        tortoise/hare meet, reset one walker to the head; advancing
        both by 1 collides exactly at the cycle entry — a = k·L − b.
        O(n) time, O(1) space.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        else:
            return None
        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        return slow


if __name__ == "__main__":
    a = ListNode(3); b = ListNode(2); c = ListNode(0); d = ListNode(-4)
    a.next = b; b.next = c; c.next = d; d.next = b
    assert Solution().detectCycle(a) is b
    assert Solution().detectCycle(ListNode(1)) is None
    print("ok")
