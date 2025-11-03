class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to simplify the logic
        dummy = ListNode(0)
        current = dummy
        
        # Compare nodes from both lists
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            # Move the current pointer forward
            current = current.next
        
        # Attach remaining nodes (if any)
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