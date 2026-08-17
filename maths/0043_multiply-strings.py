"""
Multiply Strings Solution with Explanations and Unit Tests

This file contains the solution for the Multiply Strings problem (LeetCode #43)
along with comprehensive explanations and unit tests.
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Multiply two non-negative integers represented as strings.
        
        Args:
            num1 (str): First number as string
            num2 (str): Second number as string
            
        Returns:
            str: Product of the two numbers as string
        """
        # Handle edge cases
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Initialize result array with zeros
        # Maximum possible length is len(num1) + len(num2)
        result = [0] * (len(num1) + len(num2))
        
        # Reverse both numbers for easier multiplication
        # Process from right to left (like manual multiplication)
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                # Multiply individual digits
                mul = int(num1[i]) * int(num2[j])
                
                # Calculate positions in result array
                p1 = i + j        # Position for carry
                p2 = i + j + 1    # Position for current digit
                
                # Add multiplication result to current positions
                total = mul + result[p2]
                
                # Update positions with digit and carry
                result[p2] = total % 10
                result[p1] += total // 10
        
        # Convert result array to string, skipping leading zeros
        result_str = ""
        start = 0
        while start < len(result) and result[start] == 0:
            start += 1
        
        # Build the result string
        for i in range(start, len(result)):
            result_str += str(result[i])
        
        # If all digits were zeros, return "0"
        return result_str if result_str else "0"

def run_multiply_strings_tests():
    """Run comprehensive unit tests for the Multiply Strings solution."""
    
    print("Running Unit Tests for Multiply Strings...")
    sol = Solution()
    
    # Test Case 1: Basic multiplication
    num1_1, num2_1 = "2", "3"
    expected1 = "6"
    result1 = sol.multiply(num1_1, num2_1)
    assert result1 == expected1, f"Test 1 failed: Expected {expected1}, got {result1}"
    print("✓ Test 1 Passed: '2' * '3' = '6'")
    
    # Test Case 2: Multiplication with zero
    num1_2, num2_2 = "123", "0"
    expected2 = "0"
    result2 = sol.multiply(num1_2, num2_2)
    assert result2 == expected2, f"Test 2 failed: Expected {expected2}, got {result2}"
    print("✓ Test 2 Passed: '123' * '0' = '0'")
    
    # Test Case 3: Another zero case
    num1_3, num2_3 = "0", "456"
    expected3 = "0"
    result3 = sol.multiply(num1_3, num2_3)
    assert result3 == expected3, f"Test 3 failed: Expected {expected3}, got {result3}"
    print("✓ Test 3 Passed: '0' * '456' = '0'")
    
    # Test Case 4: Standard multiplication
    num1_4, num2_4 = "123", "456"
    expected4 = "56088"
    result4 = sol.multiply(num1_4, num2_4)
    assert result4 == expected4, f"Test 4 failed: Expected {expected4}, got {result4}"
    print("✓ Test 4 Passed: '123' * '456' = '56088'")
    
    # Test Case 5: Single digit multiplication
    num1_5, num2_5 = "9", "9"
    expected5 = "81"
    result5 = sol.multiply(num1_5, num2_5)
    assert result5 == expected5, f"Test 5 failed: Expected {expected5}, got {result5}"
    print("✓ Test 5 Passed: '9' * '9' = '81'")
    
    # Test Case 6: Large numbers
    num1_6, num2_6 = "123456789", "987654321"
    expected6 = "121932631112635269"
    result6 = sol.multiply(num1_6, num2_6)
    assert result6 == expected6, f"Test 6 failed: Expected {expected6}, got {result6}"
    print("✓ Test 6 Passed: Large multiplication")
    
    # Test Case 7: One by large number
    num1_7, num2_7 = "1", "999999999"
    expected7 = "999999999"
    result7 = sol.multiply(num1_7, num2_7)
    assert result7 == expected7, f"Test 7 failed: Expected {expected7}, got {result7}"
    print("✓ Test 7 Passed: '1' * '999999999' = '999999999'")
    
    # Test Case 8: Leading zeros in result
    num1_8, num2_8 = "9133", "0"
    expected8 = "0"
    result8 = sol.multiply(num1_8, num2_8)
    assert result8 == expected8, f"Test 8 failed: Expected {expected8}, got {result8}"
    print("✓ Test 8 Passed: '9133' * '0' = '0'")
    
    # Test Case 9: Different lengths
    num1_9, num2_9 = "4988286621879152962902", "1375230538666842292227"
    expected9 = "685995615345887523535102533275774693208916587683"
    result9 = sol.multiply(num1_9, num2_9)
    assert result9 == expected9, f"Test 9 failed: Expected {expected9}, got {result9}"
    print("✓ Test 9 Passed: Very large multiplication")
    
    # Test Case 10: Edge case with 1
    num1_10, num2_10 = "456", "1"
    expected10 = "456"
    result10 = sol.multiply(num1_10, num2_10)
    assert result10 == expected10, f"Test 10 failed: Expected {expected10}, got {result10}"
    print("✓ Test 10 Passed: '456' * '1' = '456'")
    
    # Test Case 11: Another multiplication with carries
    num1_11, num2_11 = "999", "999"
    expected11 = "998001"
    result11 = sol.multiply(num1_11, num2_11)
    assert result11 == expected11, f"Test 11 failed: Expected {expected11}, got {result11}"
    print("✓ Test 11 Passed: '999' * '999' = '998001'")
    
    # Test Case 12: Different length numbers
    num1_12, num2_12 = "123", "45"
    expected12 = "5535"
    result12 = sol.multiply(num1_12, num2_12)
    assert result12 == expected12, f"Test 12 failed: Expected {expected12}, got {result12}"
    print("✓ Test 12 Passed: '123' * '45' = '5535'")
    
    print("\n🎉 All Multiply Strings tests passed! The solution works correctly.")

def explain_multiply_strings_algorithm():
    """Explain the Multiply Strings algorithm in detail."""
    
    print("\n" + "="*70)
    print("MULTIPLY STRINGS ALGORITHM EXPLANATION")
    print("="*70)
    
    print("\nWhat is Multiply Strings?")
    print("-" * 35)
    print("Given two non-negative integers num1 and num2 represented as strings,")
    print("return the product of num1 and num2, also represented as a string.")
    print("Cannot use built-in BigInteger or convert inputs to integers directly.")
    
    print("\nAlgorithm Approach: Manual Multiplication")
    print("-" * 40)
    print("The solution simulates manual multiplication (like elementary school method):")
    print("• Multiply each digit of num1 with each digit of num2")
    print("• Handle carries properly")
    print("• Store results in appropriate positions")
    
    print("\nKey Steps:")
    print("-" * 20)
    print("1. Handle edge cases (multiplication by 0)")
    print("2. Initialize result array of size len(num1) + len(num2)")
    print("3. For each digit in num1 and num2:")
    print("   - Multiply the digits")
    print("   - Add to appropriate positions in result array")
    print("   - Handle carry propagation")
    print("4. Convert result array to string, skipping leading zeros")
    
    print("\nDetailed Example: '123' * '456'")
    print("-" * 35)
    print("Step 1: Initialize result array of size 3+3=6: [0,0,0,0,0,0]")
    print("Step 2: Process each digit multiplication:")
    print("  3*6=18 → result[5]=8, carry=1 to result[4]")
    print("  2*6=12, result[4]=12+1=13 → result[4]=3, carry=1 to result[3]")
    print("  1*6=6, result[3]=6+1=7 → result[3]=7")
    print("  Continue for all digit pairs...")
    print("Final result array: [0,5,6,0,8,8] → '56088'")
    
    print("\nWhy Array Size is len(num1) + len(num2)?")
    print("-" * 45)
    print("• Maximum possible digits in product is sum of input digits")
    print("• Example: 999 * 999 = 998001 (6 digits = 3 + 3)")
    print("• Minimum possible digits is sum - 1 (when there are leading zeros)")
    
    print("\nIndex Mapping:")
    print("-" * 20)
    print("When multiplying digit at position i of num1 with digit at position j of num2:")
    print("• The result affects positions i+j and i+j+1 in the result array")
    print("• Position i+j gets the carry")
    print("• Position i+j+1 gets the units digit")
    
    print("\nCarry Handling:")
    print("-" * 20)
    print("• Add multiplication result to existing value at position")
    print("• Extract units digit: total % 10")
    print("• Propagate carry: total // 10")
    
    print("\nTime & Space Complexity:")
    print("-" * 35)
    print("Time: O(M * N) where M = len(num1), N = len(num2)")
    print("Space: O(M + N) for the result array")
    
    print("\nAlgorithm Properties:")
    print("-" * 35)
    print("• Handles all edge cases (including multiplication by 0)")
    print("• Correctly manages carries during multiplication")
    print("• Eliminates leading zeros in final result")
    print("• Works for arbitrarily large numbers")
    print("• Simulates manual multiplication process")
    
    print("\nAdvantages:")
    print("-" * 20)
    print("• No integer overflow issues")
    print("• Works with very large numbers")
    print("• Follows mathematical multiplication principles")
    print("• Efficient time complexity")
    
    print("\nAlternative Approaches:")
    print("-" * 35)
    print("• Direct conversion: Not allowed per problem constraints")
    print("• Recursive approach: More complex, same time complexity")
    print("• FFT-based: Overkill for this problem, used for very large numbers")

if __name__ == "__main__":
    # Run tests
    run_multiply_strings_tests()
    
    # Explain the algorithm
    explain_multiply_strings_algorithm()