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
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        """
        Merges two sorted linked lists into one sorted list by splicing nodes.
        
        Problem Understanding:
        - Given two sorted linked lists
        - Merge them into one sorted list
        - Return the head of the merged list
        - Do not create new nodes, just rewire existing ones
        
        Approach:
        - Use a dummy node to simplify edge case handling
        - Compare values from both lists and attach smaller one
        - Continue until one list is exhausted
        - Attach remaining nodes from the non-empty list
        
        Time Complexity: O(m + n) where m, n are lengths of the two lists
        Space Complexity: O(1) - only using constant extra space
        
        Args:
            list1: Head of first sorted linked list
            list2: Head of second sorted linked list
            
        Returns:
            Head of the merged sorted linked list
        """
        # Create a dummy node to simplify the logic and handle edge cases
        dummy = ListNode(0)
        current = dummy  # Pointer to build the result list
        
        # Compare nodes from both lists and attach the smaller one
        while list1 and list2:
            if list1.val <= list2.val:
                # Attach current node from list1
                current.next = list1
                list1 = list1.next  # Move to next node in list1
            else:
                # Attach current node from list2
                current.next = list2
                list2 = list2.next  # Move to next node in list2
            
            # Move the current pointer forward in the result list
            current = current.next
        
        # Attach remaining nodes from either list (if any)
        # Since both lists are sorted, remaining nodes are already in correct order
        current.next = list1 if list1 else list2
        
        # Return the merged list (skip the dummy node)
        return dummy.next

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

def run_merge_test(list1_arr, list2_arr, expected, test_name):
    """
    Tests the mergeTwoLists function with array inputs and outputs.
    
    Args:
        list1_arr: First sorted array to convert to linked list
        list2_arr: Second sorted array to convert to linked list
        expected: Expected merged array
        test_name: Name/description of the test case
    """
    solution = Solution()
    list1 = create_linked_list(list1_arr)
    list2 = create_linked_list(list2_arr)
    result = solution.mergeTwoLists(list1, list2)
    result_arr = linked_list_to_array(result)
    
    print(f"{test_name}:")
    print(f"  Input: list1 = {list1_arr}, list2 = {list2_arr}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result_arr}")
    print(f"  Pass: {result_arr == expected}")
    print()

# Run test cases
run_merge_test([1,2,4], [1,3,4], [1,1,2,3,4,4], "Example 1: Basic merge")
run_merge_test([], [], [], "Example 2: Both empty")
run_merge_test([], [0], [0], "Example 3: First empty")
run_merge_test([0], [], [0], "Example 4: Second empty")
run_merge_test([1,2,3], [4,5,6], [1,2,3,4,5,6], "Edge case: No overlap")
run_merge_test([4,5,6], [1,2,3], [1,2,3,4,5,6], "Edge case: Reverse order")
run_merge_test([1,1,1], [1,1,1], [1,1,1,1,1,1], "Edge case: All same values")