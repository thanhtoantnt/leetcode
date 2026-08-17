from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Partitions a string such that every substring of the partition is a palindrome.
        
        Problem Understanding:
        - Given a string s, partition s such that every substring is a palindrome
        - Return all possible palindrome partitioning of s
        
        Approach:
        - Use backtracking to explore all possible partitions
        - At each position, try all possible substrings starting from current position
        - If substring is a palindrome, add it to current partition and continue recursively
        - When we reach the end of string, add current partition to result
        - Backtrack by removing the last added substring
        
        Time Complexity: O(N * 2^N) where N is the length of string
        Space Complexity: O(N) for recursion depth (excluding output)
        
        Args:
            s: Input string to partition
            
        Returns:
            List of all possible palindrome partitions
        """
        result = []
        
        def is_palindrome(string, start, end):
            """Helper function to check if substring is palindrome"""
            while start < end:
                if string[start] != string[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        def backtrack(start, current_partition):
            # Base case: if we've processed the entire string
            if start == len(s):
                result.append(current_partition[:])  # Add a copy of current partition
                return
            
            # Try all possible substrings starting from 'start' position
            for end in range(start, len(s)):
                # If current substring is palindrome, continue with it
                if is_palindrome(s, start, end):
                    # Add current palindrome substring to partition
                    current_partition.append(s[start:end+1])
                    
                    # Recursively partition the rest of the string
                    backtrack(end + 1, current_partition)
                    
                    # Backtrack: remove the last added substring
                    current_partition.pop()
        
        backtrack(0, [])
        return result

def run_palindrome_partition_test(s, expected, test_name):
    """
    Tests the partition function.
    
    Args:
        s: Input string to partition
        expected: Expected list of palindrome partitions
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.partition(s)
    
    # Convert to sets of tuples for order-independent comparison
    result_set = set(tuple(partition) for partition in result)
    expected_set = set(tuple(partition) for partition in expected)
    
    print(f"{test_name}:")
    print(f"  Input: '{s}'")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result_set == expected_set}")
    print(f"  Count: Expected {len(expected)}, Got {len(result)}")
    print()

# Run test cases
run_palindrome_partition_test("aab", [["a","a","b"],["aa","b"]], "Example 1: 'aab' -> [['a','a','b'],['aa','b']]")
run_palindrome_partition_test("a", [["a"]], "Example 2: 'a' -> [['a']]")
run_palindrome_partition_test("ab", [["a","b"]], "Edge case: 'ab' -> [['a','b']]")
run_palindrome_partition_test("aa", [["a","a"],["aa"]], "Edge case: 'aa' -> [['a','a'],['aa']]")
run_palindrome_partition_test("aba", [["a","b","a"],["aba"]], "Edge case: 'aba' -> [['a','b','a'],['aba']]")
run_palindrome_partition_test("abc", [["a","b","c"]], "Edge case: 'abc' -> [['a','b','c']]")
run_palindrome_partition_test("aaa", [["a","a","a"],["a","aa"],["aa","a"],["aaa"]], "Edge case: 'aaa' -> multiple partitions")
run_palindrome_partition_test("abcd", [["a","b","c","d"]], "Edge case: 'abcd' -> [['a','b','c','d']]")
run_palindrome_partition_test("racecar", [["r","a","c","e","c","a","r"],["r","a","cec","a","r"],["racecar"]], "Edge case: 'racecar' -> palindromic string")
run_palindrome_partition_test("", [[]], "Edge case: Empty string -> [[]]")
run_palindrome_partition_test("abccba", [["a","b","c","c","b","a"],["a","b","cc","b","a"],["a","bccb","a"],["abccba"]], "Edge case: 'abccba' -> multiple partitions")
run_palindrome_partition_test("abcdef", [["a","b","c","d","e","f"]], "Edge case: All different -> [['a','b','c','d','e','f']]")