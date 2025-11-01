"""
Daily Coding Practice Solution
Problem: Using a Robot to Print the Lexicographically Smallest String
Date: 2025-11-01
"""

# Standard library imports
from typing import List, Optional, Dict, Set, Tuple
import collections

class Solution:
    def solve_problem(self, s: str) -> str:
        """
        Computes the lexicographically smallest string that can be written by the robot.
        
        Args:
            s (str): The input string.
            
        Returns:
            str: The lexicographically smallest string the robot can write.
            
        Time Complexity: O(n) - each character is pushed and popped at most once
        Space Complexity: O(n) - for the stack t and output string p
        """
        n = len(s)
        
        # Precompute the smallest remaining character from i to end
        min_suff = [None] * n
        min_suff[-1] = s[-1]
        for i in range(n-2, -1, -1):
            min_suff[i] = min(s[i], min_suff[i+1])
        
        t = []  # robot's stack
        p = []  # output string
        i = 0
        
        while i < n or t:
            if t and (i == n or t[-1] <= min_suff[i]):
                p.append(t.pop())
            else:
                t.append(s[i])
                i += 1
        
        return "".join(p)


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test Case 1: Example 1
    input1 = "zza"
    expected1 = "azz"
    result1 = solution.solve_problem(input1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print("✓ Test 1 passed")
    
    # Test Case 2: Example 2
    input2 = "bac"
    expected2 = "abc"
    result2 = solution.solve_problem(input2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print("✓ Test 2 passed")
    
    # Test Case 3: Example 3
    input3 = "bdda"
    expected3 = "addb"
    result3 = solution.solve_problem(input3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print("✓ Test 3 passed")
    
    # Test Case 4: Edge case - single character
    input4 = "a"
    expected4 = "a"
    result4 = solution.solve_problem(input4)
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print("✓ Test 4 passed")
    
    # Test Case 5: Edge case - already sorted
    input5 = "abcde"
    expected5 = "abcde"
    result5 = solution.solve_problem(input5)
    assert result5 == expected5, f"Test 5 failed: expected {expected5}, got {result5}"
    print("✓ Test 5 passed")
    
    print("All tests passed! ✅")


def main():
    """Main execution function"""
    print("Running solution tests...")
    test_solution()
    
    # Optional: Run with custom input
    # solution = Solution()
    # custom_input = "your_input_here"
    # result = solution.solve_problem(custom_input)
    # print(f"Result: {result}")


if __name__ == "__main__":
    main()