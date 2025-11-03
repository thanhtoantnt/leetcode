from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups anagrams from the input list.
        
        Approach:
        - For each string, sort its characters to create a canonical form
        - Use the sorted string as a key in a hash table
        - All strings that are anagrams will have the same sorted form
        - Group all original strings under their canonical form key
        
        Time Complexity: O(N * M * log M) where N is number of strings and M is average string length
        Space Complexity: O(N * M) for storing the result and hash table
        """
        # Hash table to store groups of anagrams
        # Key: sorted string (canonical form), Value: list of original strings
        htbl = {}

        for word in strs:
            # Create canonical form by sorting characters
            # All anagrams will have the same sorted form
            key = "".join(sorted(word))
            
            # Initialize empty list if key doesn't exist
            if key not in htbl:
                htbl[key] = []

            # Add current word to its anagram group
            htbl[key].append(word)

        # Return all groups as a list of lists
        return list(htbl.values())

def run_anagram_test(strs, expected, test_name):
    """
    Tests the groupAnagrams function with order-independent comparison.
    
    Args:
        strs: Input list of strings to group
        expected: Expected result (list of anagram groups)
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.groupAnagrams(strs)
    
    # Convert to sets of tuples for order-independent comparison
    # This handles cases where group order or internal order differs but result is valid
    result_set = set(tuple(sorted(group)) for group in result)
    expected_set = set(tuple(sorted(group)) for group in expected)
    
    print(f"{test_name}:")
    print(f"  Input: {strs}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result_set == expected_set}")
    print()

# Run test cases
run_anagram_test(["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]], "Example 1: Basic anagrams")
run_anagram_test([""], [[""]], "Example 2: Empty string")
run_anagram_test(["a"], [["a"]], "Example 3: Single character")
run_anagram_test(["abc","bca","cab","xyz","zyx","yxz"], [["abc","bca","cab"],["xyz","zyx","yxz"]], "Edge case: Multiple anagram groups")
run_anagram_test(["abc","def","ghi"], [["abc"],["def"],["ghi"]], "Edge case: No anagrams")
run_anagram_test(["listen","silent","enlist","hello"], [["hello"],["listen","silent","enlist"]], "Edge case: Longer words")
run_anagram_test(["aab","aba","baa","xyz"], [["xyz"],["aab","aba","baa"]], "Edge case: Repeated characters")
run_anagram_test([], [], "Edge case: Empty list")
run_anagram_test(["abc","abc","abc"], [["abc","abc","abc"]], "Edge case: All same words")
run_anagram_test(["abc","def","abc","def"], [["abc","abc"],["def","def"]], "Edge case: Duplicates")