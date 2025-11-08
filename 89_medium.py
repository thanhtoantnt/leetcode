"""
Gray Code Solution with Explanations and Unit Tests

This file contains the solution for the Gray Code problem
along with comprehensive explanations and unit tests.
"""

from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        """
        Generate the Gray code sequence for n bits.
        
        A Gray code sequence is a sequence of 2^n integers where:
        - Every integer is in the inclusive range [0, 2^n - 1]
        - The first integer is 0
        - Each integer appears only once
        - Adjacent integers differ by exactly one bit
        - The first and last integers differ by exactly one bit
        
        Args:
            n (int): Number of bits for the Gray code sequence
            
        Returns:
            List[int]: The Gray code sequence
        """
        # Handle edge case: if n is 0, return empty list
        if n == 0:
            return [0]  # Actually, for n=0, it should be [0] as per definition
        
        # Initialize with 1-bit Gray code: ["0", "1"]
        elements = ["0", "1"]
        
        # Build Gray code for 2 to n bits using the recursive pattern
        for _ in range(1, n):
            new_list = []
            
            # Add prefix "0" to all elements in original order
            for element in elements:
                new_list.append("0" + element)
            
            # Add prefix "1" to all elements in reverse order
            for element in reversed(elements):
                new_list.append("1" + element)
            
            # Update elements for next iteration
            elements = new_list
        
        # Convert binary string representations to integers
        return [int(element, 2) for element in elements]

def run_gray_code_tests():
    """Run comprehensive unit tests for the Gray Code solution."""
    
    print("Running Unit Tests for Gray Code...")
    sol = Solution()
    
    # Test Case 1: n = 0
    result1 = sol.grayCode(0)
    expected1 = [0]
    assert result1 == expected1, f"Test 1 failed: Expected {expected1}, got {result1}"
    print("✓ Test 1 Passed: n = 0")
    
    # Test Case 2: n = 1
    result2 = sol.grayCode(1)
    expected2 = [0, 1]  # Binary: ["0", "1"]
    assert result2 == expected2, f"Test 2 failed: Expected {expected2}, got {result2}"
    print("✓ Test 2 Passed: n = 1")
    
    # Test Case 3: n = 2
    result3 = sol.grayCode(2)
    expected3 = [0, 1, 3, 2]  # Binary: ["00", "01", "11", "10"]
    assert result3 == expected3, f"Test 3 failed: Expected {expected3}, got {result3}"
    # Verify adjacent elements differ by exactly one bit
    for i in range(len(result3)):
        j = (i + 1) % len(result3)  # Next element (circular)
        xor_result = result3[i] ^ result3[j]
        # Check if xor_result is a power of 2 (has exactly one bit set)
        assert (xor_result & (xor_result - 1)) == 0, f"Test 3 failed: Adjacent elements {result3[i]} and {result3[j]} don't differ by one bit"
    print("✓ Test 3 Passed: n = 2 with proper bit differences")
    
    # Test Case 4: n = 3
    result4 = sol.grayCode(3)
    expected4 = [0, 1, 3, 2, 6, 7, 5, 4]  # Binary: ["000", "001", "011", "010", "110", "111", "101", "100"]
    assert result4 == expected4, f"Test 4 failed: Expected {expected4}, got {result4}"
    # Verify adjacent elements differ by exactly one bit
    for i in range(len(result4)):
        j = (i + 1) % len(result4)  # Next element (circular)
        xor_result = result4[i] ^ result4[j]
        assert (xor_result & (xor_result - 1)) == 0, f"Test 4 failed: Adjacent elements {result4[i]} and {result4[j]} don't differ by one bit"
    print("✓ Test 4 Passed: n = 3 with proper bit differences")
    
    # Test Case 5: Verify sequence length
    for n in [0, 1, 2, 3, 4]:
        result = sol.grayCode(n)
        expected_length = 2 ** n
        assert len(result) == expected_length, f"Test 5 failed for n={n}: Expected length {expected_length}, got {len(result)}"
    print("✓ Test 5 Passed: All sequence lengths correct")
    
    # Test Case 6: Verify first element is always 0
    for n in [0, 1, 2, 3, 4]:
        result = sol.grayCode(n)
        assert result[0] == 0, f"Test 6 failed for n={n}: First element should be 0, got {result[0]}"
    print("✓ Test 6 Passed: First element is always 0")
    
    # Test Case 7: Verify all numbers are unique
    for n in [0, 1, 2, 3]:
        result = sol.grayCode(n)
        unique_count = len(set(result))
        assert unique_count == len(result), f"Test 7 failed for n={n}: Not all elements are unique"
        # Verify all numbers are in range [0, 2^n - 1]
        max_val = 2 ** n - 1
        for num in result:
            assert 0 <= num <= max_val, f"Test 7 failed for n={n}: Number {num} is out of range [0, {max_val}]"
    print("✓ Test 7 Passed: All elements are unique and in valid range")
    
    # Test Case 8: Verify circular property (first and last differ by one bit)
    for n in [1, 2, 3]:
        result = sol.grayCode(n)
        first, last = result[0], result[-1]
        xor_result = first ^ last
        assert (xor_result & (xor_result - 1)) == 0, f"Test 8 failed for n={n}: First {first} and last {last} don't differ by one bit"
    print("✓ Test 8 Passed: Circular property maintained")
    
    print("\n🎉 All Gray Code tests passed! The solution works correctly.")

def explain_gray_code_concept():
    """Explain the Gray code concept and the algorithm."""
    
    print("\n" + "="*60)
    print("GRAY CODE EXPLANATION")
    print("="*60)
    
    print("\nWhat is Gray Code?")
    print("-" * 20)
    print("Gray code is a binary numeral system where two successive values differ in only one bit.")
    print("This is useful in applications where transitions between states should be minimized.")
    
    print("\nGray Code Properties:")
    print("-" * 20)
    print("1. Each integer appears exactly once")
    print("2. Adjacent integers differ by exactly one bit")
    print("3. The first and last integers also differ by exactly one bit")
    print("4. Contains 2^n numbers for n bits")
    print("5. Always starts with 0")
    
    print("\nConstruction Pattern (Recursive):")
    print("-" * 20)
    print("For n bits, we can construct from (n-1) bit Gray code:")
    print("1. Take the (n-1)-bit Gray code sequence")
    print("2. Prefix all elements with '0' in original order")
    print("3. Prefix all elements with '1' in reverse order")
    print("4. Concatenate both sequences")
    
    print("\nExample Construction:")
    print("-" * 20)
    print("n=1: [0, 1] → [\"0\", \"1\"]")
    print("n=2: Take [\"0\", \"1\"]")
    print("       Prefix with '0': [\"00\", \"01\"]")
    print("       Prefix with '1' in reverse: [\"11\", \"10\"]")
    print("       Combined: [\"00\", \"01\", \"11\", \"10\"] → [0, 1, 3, 2]")
    print("n=3: Take [\"00\", \"01\", \"11\", \"10\"]")
    print("       Prefix with '0': [\"000\", \"001\", \"011\", \"010\"]")
    print("       Prefix with '1' in reverse: [\"110\", \"111\", \"101\", \"100\"]")
    print("       Combined: [\"000\", \"001\", \"011\", \"010\", \"110\", \"111\", \"101\", \"100\"] → [0, 1, 3, 2, 6, 7, 5, 4]")
    
    print("\nAlgorithm Complexity:")
    print("-" * 20)
    print("Time: O(2^n) - We generate 2^n numbers")
    print("Space: O(2^n) - We store 2^n numbers")
    
    print("\nBinary Representations:")
    print("-" * 20)
    for n in [1, 2, 3]:
        result = Solution().grayCode(n)
        print(f"n={n}: {result}")
        binary_repr = [format(num, f'0{n}b') for num in result]
        print(f"     : {binary_repr}")

if __name__ == "__main__":
    # Run the original example
    sol = Solution()
    print("Original example (n=2):", sol.grayCode(2))
    
    # Run tests
    run_gray_code_tests()
    
    # Explain the concept
    explain_gray_code_concept()