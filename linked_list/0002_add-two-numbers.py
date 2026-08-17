class ListNode:
    def __init__(self, val=0, next=None):
        """
        Definition for singly-linked list node.
        
        Args:
            val: Value stored in the node
            next: Reference to the next node in the list
        """
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
        """
        Adds two numbers represented as linked lists in reverse order.
        
        Problem Understanding:
        - Each node contains a single digit
        - Digits are stored in reverse order (least significant first)
        - Add the two numbers and return the sum as a linked list
        - Handle carry propagation between digits
        
        Approach:
        - Use a dummy head to simplify edge cases
        - Process both lists simultaneously
        - Maintain carry for sums >= 10
        - Continue until both lists are processed and no carry remains
        
        Time Complexity: O(max(m, n)) where m, n are lengths of the two lists
        Space Complexity: O(max(m, n)) for the result list
        
        Args:
            l1: First number as linked list (reverse order)
            l2: Second number as linked list (reverse order)
            
        Returns:
            Sum as linked list in reverse order
        """
        # Dummy node to simplify edge case handling
        dummy = ListNode(0)
        current = dummy
        
        # Carry to store overflow from digit addition
        carry = 0
        
        # Continue while either list has nodes or there's a carry
        while l1 or l2 or carry:
            # Get current digits (0 if list is exhausted)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum with carry from previous position
            total = val1 + val2 + carry
            
            # Current digit to store (0-9)
            digit = total % 10
            
            # Carry for next iteration (0 or 1)
            carry = total // 10
            
            # Create new node with the digit
            current.next = ListNode(digit)
            current = current.next
            
            # Move to next nodes if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Return the actual result (skip dummy head)
        return dummy.next

# Test Cases
def run_test_case(l1_arr, l2_arr, expected_arr, test_name):
    """
    Tests the addTwoNumbers function with array inputs and outputs.
    
    Args:
        l1_arr: First number as array (reverse order)
        l2_arr: Second number as array (reverse order)  
        expected_arr: Expected sum as array (reverse order)
        test_name: Name/description of the test case
    """
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
run_test_case([2,4,3], [5,6,4], [7,0,8], "Example 1: Basic addition (342 + 465 = 807)")
run_test_case([0], [0], [0], "Example 2: Zeros (0 + 0 = 0)")
run_test_case([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1], "Example 3: Carry propagation (9999999 + 9999 = 10009998)")
run_test_case([1], [9,9], [0,0,1], "Test case: Different lengths with carry (1 + 99 = 100)")
run_test_case([5], [5], [0,1], "Test case: Single digits with carry (5 + 5 = 10)")
run_test_case([1,8], [0], [1,8], "Test case: One list empty (81 + 0 = 81)")
run_test_case([9,9,9], [1], [0,0,0,1], "Test case: Final carry creates new digit (999 + 1 = 1000)")