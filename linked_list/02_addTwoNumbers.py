class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    """Helper function to create a linked list from array"""
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

def linked_list_to_array(head):
    """Helper function to convert linked list back to array for easy verification"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Continue while either list has nodes or there's a carry
        while l1 or l2 or carry:
            # Get current digits (0 if list is exhausted)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum with carry
            total = val1 + val2 + carry
            digit = total % 10  # Current digit to store
            carry = total // 10  # Carry for next iteration
            
            # Create new node with the digit
            current.next = ListNode(digit)
            current = current.next
            
            # Move to next nodes if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next

# Test Cases
def run_test_case(l1_arr, l2_arr, expected_arr, test_name):
    solution = Solution()
    
    l1 = create_linked_list(l1_arr)
    l2 = create_linked_list(l2_arr)
    
    result = solution.addTwoNumbers(l1, l2)
    result_arr = linked_list_to_array(result)
    
    print(f"{test_name}:")
    print(f"  Input: l1 = {l1_arr}, l2 = {l2_arr}")
    print(f"  Expected: {expected_arr}")
    print(f"  Got: {result_arr}")
    print(f"  Pass: {result_arr == expected_arr}")
    print()

# Run all test cases
run_test_case([2,4,3], [5,6,4], [7,0,8], "Example 1: Basic addition")
run_test_case([0], [0], [0], "Example 2: Zeros")
run_test_case([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1], "Example 3: Carry propagation")
run_test_case([1], [9,9], [0,0,1], "Test case: Different lengths with carry")
run_test_case([5], [5], [0,1], "Test case: Single digits with carry")
run_test_case([1,8], [0], [1,8], "Test case: One list empty")
run_test_case([9,9,9], [1], [0,0,0,1], "Test case: Final carry creates new digit")