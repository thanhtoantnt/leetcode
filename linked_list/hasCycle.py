class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def create_linked_list(arr):
    """Create a linked list from array (no cycle)"""
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

def create_cycled_list(arr, pos):
    """
    Create a linked list with cycle
    pos: index where tail connects to (or -1 for no cycle)
    """
    if not arr or pos == -1:
        return create_linked_list(arr)
    
    head = ListNode(arr[0])
    nodes = [head]
    current = head
    
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
        nodes.append(current)
    
    # Create cycle: connect tail to nodes[pos]
    if 0 <= pos < len(nodes):
        current.next = nodes[pos]
    
    return head

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        
        slow = head
        fast = head
        
        # Move slow one step, fast two steps
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If they meet, there's a cycle
            if slow == fast:
                return True
        
        # If fast reaches NULL, no cycle exists
        return False

def run_test_case(arr, pos, expected, test_name):
    solution = Solution()
    head = create_cycled_list(arr, pos)
    result = solution.hasCycle(head)
    
    print(f"{test_name}:")
    print(f"  Input: {arr}, pos = {pos}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run all test cases
run_test_case([3,2,0,-4], 1, True, "Example 1: Cycle at index 1")
run_test_case([1,2], 0, True, "Example 2: Cycle at index 0") 
run_test_case([1], -1, False, "Example 3: Single node, no cycle")
run_test_case([1], 0, True, "Edge case: Single node with self-cycle")
run_test_case([1,2], -1, False, "Edge case: Two nodes, no cycle")
run_test_case([1,2,3,4], 2, True, "Edge case: Cycle in middle")
run_test_case([1,2,3,4], 3, True, "Edge case: Cycle to last node")
run_test_case([1,2,3,4], -1, False, "Edge case: No cycle, longer list")
run_test_case([], -1, False, "Edge case: Empty list")
run_test_case([1,1], 0, True, "Edge case: Duplicates with cycle")