from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Merge k sorted linked lists.

        Min-heap of (head val, index): pop the smallest head, append it,
        push its successor. Each node enters/leaves the heap once:
        O(N log k) where N = total nodes, k = list count.
        """
        import heapq

        heap = [(node.val, i) for i, node in enumerate(lists) if node]
        heapq.heapify(heap)
        dummy = tail = ListNode()
        while heap:
            _, i = heapq.heappop(heap)
            node = lists[i]
            tail.next = node
            tail = tail.next
            if node.next:
                lists[i] = node.next
                heapq.heappush(heap, (node.next.val, i))
        return dummy.next


if __name__ == "__main__":
    def build(vals):
        h = ListNode(); c = h
        for v in vals:
            c.next = ListNode(v); c = c.next
        return h.next
    def flat(h):
        out = []
        while h:
            out.append(h.val); h = h.next
        return out
    r = Solution().mergeKLists([build([1, 4, 5]), build([1, 3, 4]), build([2, 6])])
    assert flat(r) == [1, 1, 2, 3, 4, 4, 5, 6]
    print("ok")
