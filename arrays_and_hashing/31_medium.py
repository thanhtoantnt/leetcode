"""
Next Permutation Solution with Explanations and Unit Tests

This file contains the solution for the Next Permutation problem
along with comprehensive explanations and unit tests.
"""

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modify nums in-place to form the next lexicographically greater permutation.
        
        The algorithm works in three steps:
        1. Find the pivot: rightmost position where nums[i] < nums[i+1]
        2. If pivot exists, find successor and swap
        3. Reverse the suffix after pivot position
        
        Args:
            nums (List[int]): The input array to modify in-place
        """
        if nums == []:
            return
        
        # Step 1: Find the pivot from right to left
        # The pivot is the rightmost position where nums[i] < nums[i+1]
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2: If pivot exists, find the smallest number greater than pivot
        # to the right and swap them
        if i >= 0:
            j = len(nums) - 1
            # Find rightmost element greater than nums[i]
            while nums[j] <= nums[i]:
                j = j - 1
            # Swap pivot with its successor
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the suffix after the pivot position
        # This ensures the smallest possible arrangement for the remaining part
        left = i + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

def run_next_permutation_tests():
    """Run comprehensive unit tests for the Next Permutation solution."""
    
    print("Running Unit Tests for Next Permutation...")
    sol = Solution()
    
    # Test Case 1: Basic case with next permutation
    nums1 = [1, 2, 3]
    expected1 = [1, 3, 2]
    sol.nextPermutation(nums1)
    assert nums1 == expected1, f"Test 1 failed: Expected {expected1}, got {nums1}"
    print("✓ Test 1 Passed: [1,2,3] → [1,3,2]")
    
    # Test Case 2: Largest permutation (wrap around to smallest)
    nums2 = [3, 2, 1]
    expected2 = [1, 2, 3]
    sol.nextPermutation(nums2)
    assert nums2 == expected2, f"Test 2 failed: Expected {expected2}, got {nums2}"
    print("✓ Test 2 Passed: [3,2,1] → [1,2,3] (wrap around)")
    
    # Test Case 3: Medium case
    nums3 = [1, 1, 5]
    expected3 = [1, 5, 1]
    sol.nextPermutation(nums3)
    assert nums3 == expected3, f"Test 3 failed: Expected {expected3}, got {nums3}"
    print("✓ Test 3 Passed: [1,1,5] → [1,5,1]")
    
    # Test Case 4: Next permutation with multiple digits
    nums4 = [1, 3, 2]
    expected4 = [2, 1, 3]
    sol.nextPermutation(nums4)
    assert nums4 == expected4, f"Test 4 failed: Expected {expected4}, got {nums4}"
    print("✓ Test 4 Passed: [1,3,2] → [2,1,3]")
    
    # Test Case 5: Four elements
    nums5 = [1, 2, 3, 4]
    expected5 = [1, 2, 4, 3]
    sol.nextPermutation(nums5)
    assert nums5 == expected5, f"Test 5 failed: Expected {expected5}, got {nums5}"
    print("✓ Test 5 Passed: [1,2,3,4] → [1,2,4,3]")
    
    # Test Case 6: Another four elements
    nums6 = [1, 2, 4, 3]
    expected6 = [1, 3, 2, 4]
    sol.nextPermutation(nums6)
    assert nums6 == expected6, f"Test 6 failed: Expected {expected6}, got {nums6}"
    print("✓ Test 6 Passed: [1,2,4,3] → [1,3,2,4]")
    
    # Test Case 7: Largest 4-element permutation
    nums7 = [4, 3, 2, 1]
    expected7 = [1, 2, 3, 4]
    sol.nextPermutation(nums7)
    assert nums7 == expected7, f"Test 7 failed: Expected {expected7}, got {nums7}"
    print("✓ Test 7 Passed: [4,3,2,1] → [1,2,3,4] (wrap around)")
    
    # Test Case 8: Duplicate elements
    nums8 = [1, 5, 1]
    expected8 = [5, 1, 1]
    sol.nextPermutation(nums8)
    assert nums8 == expected8, f"Test 8 failed: Expected {expected8}, got {nums8}"
    print("✓ Test 8 Passed: [1,5,1] → [5,1,1]")
    
    # Test Case 9: Two elements
    nums9 = [1, 3]
    expected9 = [3, 1]
    sol.nextPermutation(nums9)
    assert nums9 == expected9, f"Test 9 failed: Expected {expected9}, got {nums9}"
    print("✓ Test 9 Passed: [1,3] → [3,1]")
    
    # Test Case 10: Two elements - largest
    nums10 = [3, 1]
    expected10 = [1, 3]
    sol.nextPermutation(nums10)
    assert nums10 == expected10, f"Test 10 failed: Expected {expected10}, got {nums10}"
    print("✓ Test 10 Passed: [3,1] → [1,3] (wrap around)")
    
    # Test Case 11: Empty array
    nums11 = []
    expected11 = []
    sol.nextPermutation(nums11)
    assert nums11 == expected11, f"Test 11 failed: Expected {expected11}, got {nums11}"
    print("✓ Test 11 Passed: [] → [] (empty array)")
    
    # Test Case 12: Single element
    nums12 = [1]
    expected12 = [1]
    sol.nextPermutation(nums12)
    assert nums12 == expected12, f"Test 12 failed: Expected {expected12}, got {nums12}"
    print("✓ Test 12 Passed: [1] → [1] (single element)")
    
    # Test Case 13: Complex case
    nums13 = [1, 3, 2, 4, 1]
    expected13 = [1, 3, 4, 1, 2]
    sol.nextPermutation(nums13)
    assert nums13 == expected13, f"Test 13 failed: Expected {expected13}, got {nums13}"
    print("✓ Test 13 Passed: [1,3,2,4,1] → [1,3,4,1,2]")
    
    print("\n🎉 All Next Permutation tests passed! The solution works correctly.")

def explain_next_permutation_algorithm():
    """Explain the Next Permutation algorithm in detail."""
    
    print("\n" + "="*70)
    print("NEXT PERMUTATION ALGORITHM EXPLANATION")
    print("="*70)
    
    print("\nWhat is Next Permutation?")
    print("-" * 30)
    print("Given an array, find the next lexicographically greater permutation.")
    print("If no such permutation exists, return the smallest permutation (sorted in ascending order).")
    
    print("\nAlgorithm Steps:")
    print("-" * 30)
    print("1. Find the 'pivot' - rightmost position where nums[i] < nums[i+1]")
    print("2. If pivot exists, find the 'successor' - smallest number to the right of pivot that's greater than pivot")
    print("3. Swap pivot and successor")
    print("4. Reverse the suffix after original pivot position")
    
    print("\nWhy This Algorithm Works:")
    print("-" * 30)
    print("• Finding rightmost pivot ensures we change the rightmost possible position")
    print("• Swapping with smallest successor ensures next greater permutation")
    print("• Reversing suffix ensures smallest possible arrangement for remaining part")
    
    print("\nDetailed Example: [1,3,2,4,1] → [1,3,4,1,2]")
    print("-" * 50)
    print("Step 1 - Find pivot: [1,3,2,4,1]")
    print("  Check from right: 1<4? Yes → pivot at index 3 (value 4)")
    print("  Wait, let's be more careful:")
    print("  nums[4]=1, nums[3]=4 → 1<4? No")
    print("  nums[3]=4, nums[2]=2 → 4<2? No") 
    print("  nums[2]=2, nums[1]=3 → 2<3? No")
    print("  nums[1]=3, nums[0]=1 → 3<1? No")
    print("  Actually, nums[0]=1 < nums[1]=3 → pivot at index 0 (value 1)")
    print("  No, let me reconsider...")
    print("  We want rightmost i where nums[i] < nums[i+1]")
    print("  i=3: nums[3]=4, nums[4]=1 → 4<1? No")
    print("  i=2: nums[2]=2, nums[3]=4 → 2<4? Yes! Pivot at index 2 (value 2)")
    
    print("\nStep 2 - Find successor to 2 in [4,1]: smallest number > 2 is 4")
    print("  But 4 is at index 3, and we want smallest number > 2 to the right of index 2")
    print("  In [4,1], only 4 > 2, so successor is 4 at index 3")
    
    print("\nStep 3 - Swap: [1,3,4,2,1]")
    print("  Swap nums[2]=2 and nums[3]=4")
    
    print("\nStep 4 - Reverse suffix after index 2: [1,3,4,1,2]")
    print("  Reverse [2,1] to get [1,2]")
    print("  Final result: [1,3,4,1,2]")
    
    print("\nEdge Case - Largest Permutation:")
    print("-" * 30)
    print("When no pivot exists (array in descending order), reverse entire array")
    print("Example: [3,2,1] → [1,2,3]")
    
    print("\nTime & Space Complexity:")
    print("-" * 30)
    print("Time: O(n) - At most three passes through the array")
    print("Space: O(1) - Only use constant extra space, modify in-place")
    
    print("\nAlgorithm Properties:")
    print("-" * 30)
    print("• Modifies array in-place")
    print("• Handles all edge cases (empty, single element, largest permutation)")
    print("• Always produces lexicographically next permutation")
    print("• Most efficient approach for this problem")

if __name__ == "__main__":
    # Run tests
    run_next_permutation_tests()
    
    # Explain the algorithm
    explain_next_permutation_algorithm()