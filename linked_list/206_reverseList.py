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

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Reverses a singly linked list iteratively.
        
        Problem Understanding:
        - Given the head of a linked list
        - Reverse the direction of all pointers
        - Return the new head of the reversed list
        
        Approach:
        - Use three pointers: previous, current, and next_temp
        - Iterate through the list, reversing each link
        - Maintain references to avoid losing nodes during reversal
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(1) - only using constant extra space
        
        Args:
            head: Head of the original linked list
            
        Returns:
            Head of the reversed linked list
        """
        # Initialize previous pointer as None (will be the new tail)
        prev = None
        # Initialize current pointer at the head
        current = head
        
        # Traverse the original list
        while current:
            # Store the next node before we lose reference (after reversing current.next)
            next_temp = current.next
            
            # Reverse the link: current node now points to previous node
            current.next = prev
            
            # Move pointers forward for next iteration
            prev = current      # Previous becomes current
            current = next_temp # Current becomes the stored next node
        
        # prev is now the new head of the reversed list
        # (the original tail is now the head)
        return prev
    
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

def run_reverse_test(arr, expected, test_name):
    """
    Tests the reverseList function with array inputs and outputs.
    
    Args:
        arr: Input array to create linked list
        expected: Expected result array after reversal
        test_name: Name/description of the test case
    """
    solution = Solution()
    head = create_linked_list(arr)
    result = solution.reverseList(head)
    result_arr = linked_list_to_array(result)
    
    print(f"{test_name}:")
    print(f"  Input: {arr}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result_arr}")
    print(f"  Pass: {result_arr == expected}")
    print()

# Run test cases
run_reverse_test([1,2,3,4,5], [5,4,3,2,1], "Example 1: Basic reversal")
run_reverse_test([1,2], [2,1], "Example 2: Two elements")
run_reverse_test([], [], "Example 3: Empty list")
run_reverse_test([1], [1], "Example 4: Single element")
run_reverse_test([1,2,3], [3,2,1], "Edge case: Three elements")