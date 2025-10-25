from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return head
        
        tmp = head
        llen = 0
        while tmp != None:
            llen += 1
            tmp = tmp.next

        assert(llen >= n)

        pos = llen - n
        if pos == 0:
            return head.next
        
        new_head = head
        while pos > 1:
            new_head = new_head.next
            pos = pos - 1
        
        removed = new_head.next
        new_head.next = removed.next

        return head

class SolutionOpt:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # First pass: get length
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Calculate position from start (0-indexed)
        target_pos = length - n
        
        # If removing the head
        if target_pos == 0:
            return head.next
        
        # Second pass: find node before the target
        current = head
        for _ in range(target_pos - 1):
            current = current.next
        
        # Remove the target node
        current.next = current.next.next
        
        return head

def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next
    print()

if __name__ == "__main__":
    sol = Solution()
    print(print_linked_list(sol.removeNthFromEnd(create_linked_list([1,2,3,4,5]), 2)))