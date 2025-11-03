class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    """Create a linked list from array"""
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

def linked_list_to_array(head):
    """Convert linked list back to array for easy verification"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Create a dummy node to handle edge cases (like removing head)
        dummy = ListNode(0)
        dummy.next = head
        
        slow = fast = dummy
        
        # Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next
            
            # This handles the case where n equals the length of the list
            if not fast:
                break
        
        # Move both pointers until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next
        
        # Remove the nth node from the end
        slow.next = slow.next.next
        
        # Return the original head
        return dummy.next

def run_test_case(arr, n, expected, test_name):
    solution = Solution()
    head = create_linked_list(arr)
    result = solution.removeNthFromEnd(head, n)
    result_arr = linked_list_to_array(result)
    
    print(f"{test_name}:")
    print(f"  Input: {arr}, n = {n}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result_arr}")
    print(f"  Pass: {result_arr == expected}")
    print()

# Run all test cases
run_test_case([1,2,3,4,5], 2, [1,2,3,5], "Example 1: Remove 2nd from end")
run_test_case([1], 1, [], "Example 2: Remove single node")
run_test_case([1,2], 1, [1], "Example 3: Remove last node")
run_test_case([1,2], 2, [2], "Edge case: Remove first node")
run_test_case([1,2,3], 3, [2,3], "Edge case: Remove first node (longer list)")
run_test_case([1,2,3,4,5], 1, [1,2,3,4], "Edge case: Remove last node (longer list)")
run_test_case([1,2,3,4,5], 5, [2,3,4,5], "Edge case: Remove first node (n equals length)")
run_test_case([1,2,3,4,5,6,7,8,9,10], 4, [1,2,3,4,5,6,8,9,10], "Edge case: Medium length list")