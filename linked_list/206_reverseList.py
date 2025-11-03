class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        
        while current:
            # Store the next node before we lose reference
            next_temp = current.next
            
            # Reverse the link
            current.next = prev
            
            # Move pointers forward
            prev = current
            current = next_temp
        
        # prev is now the new head of the reversed list
        return prev
    
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

def linked_list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def run_reverse_test(arr, expected, test_name):
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