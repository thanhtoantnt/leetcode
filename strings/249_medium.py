from typing import List
from collections import defaultdict

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        """
        Groups together all strings that belong to the same shifting sequence.
        
        Problem Understanding:
        - A shift operation moves each character to the next (or previous) in the alphabet
        - 'z' shifts to 'a' (and vice versa for backward shifts)
        - Strings belong to the same sequence if one can be transformed into another via shifts
        - Need to group all strings from the same sequence together
        
        Approach:
        - For each string, calculate a "signature" based on the relative differences between characters
        - The signature represents the pattern of shifts needed to get from the first character to each subsequent character
        - Use modulo 26 to handle wraparound (e.g., 'z' to 'a')
        - Group strings by their signature using a hash map
        - Return the grouped lists
        
        Time Complexity: O(n * m) where n is the number of strings and m is the average string length
        Space Complexity: O(n * m) for the result and hash map
        
        Args:
            strings: List of strings to be grouped
            
        Returns:
            List of lists, where each inner list contains strings from the same shifting sequence
        """
        # Hash map to group strings by their signature
        groups = defaultdict(list)
        
        for s in strings:
            # Calculate signature: differences between consecutive characters (with wraparound)
            # Normalize by the first character's value to make 'a' based shifts
            signature = []
            base_char = s[0]
            
            for char in s:
                # Calculate the shift needed to get from base_char to current char
                # Using modulo 26 handles wraparound (e.g., 'a' - 'z' = 1)
                shift = (ord(char) - ord(base_char)) % 26
                signature.append(shift)
            
            # Convert signature to tuple so it can be used as a dictionary key
            signature_tuple = tuple(signature)
            groups[signature_tuple].append(s)
        
        # Return the grouped strings
        return list(groups.values())

def run_group_strings_test(strings, expected, test_name):
    """
    Tests the groupStrings function.
    
    Args:
        strings: List of strings to be grouped
        expected: Expected grouped result (order within groups and between groups doesn't matter)
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.groupStrings(strings)
    
    # Convert both result and expected to sets of sorted tuples for comparison
    # This handles the fact that group order and order within groups might vary
    result_set = set(tuple(sorted(group)) for group in result)
    expected_set = set(tuple(sorted(group)) for group in expected)
    
    print(f"{test_name}:")
    print(f"  Input: {strings}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result_set == expected_set}")
    print()

# Run test cases
run_group_strings_test(
    ["abc","bcd","acef","xyz","az","ba","a","z"],
    [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]],
    "Example 1: Group shifting sequences"
)
run_group_strings_test(
    ["a"],
    [["a"]],
    "Example 2: Single string"
)
run_group_strings_test(
    ["abc", "def", "xyz", "def"],
    [["abc", "def"], ["xyz"]],
    "Edge case: Multiple strings in same group"
)
run_group_strings_test(
    ["abc", "def", "xyz", "aab"],
    [["abc"], ["def"], ["xyz"], ["aab"]],
    "Edge case: All different sequences"
)
run_group_strings_test(
    [],
    [],
    "Edge case: Empty input"
)
run_group_strings_test(
    ["a", "b", "c"],
    [["a", "b", "c"]],
    "Edge case: Single character strings"
)
run_group_strings_test(
    ["aa", "bb", "cc"],
    [["aa", "bb", "cc"]],
    "Edge case: Repeated characters"
)
run_group_strings_test(
    ["ab", "ba"],
    [["ab", "ba"]],
    "Edge case: Circular shift example"
)