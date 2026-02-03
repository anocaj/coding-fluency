"""
Daily Coding Practice Solution
Problem: [Problem Name]
Date: 2026-02-03
"""

# Standard library imports
from typing import List, Optional, Dict, Set, Tuple
from collections import deque
import collections
import heapq
import bisect

# Additional imports as needed
# import math
# import itertools
# import functools


class Solution:
    def orangesRotting(self, grid):
        rows,cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        
        minutes = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            level_size = len(q)
            rotted_this_round = False

            for _ in range(level_size):
                r,c = q.popleft()

                for dr,dc in directions:
                    nr,nc = r + dr, c + dc
                    if(0 <= nr < rows and 0<=nc < cols and grid[nr][nc]==1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
                        rotted_this_round = True
            if rotted_this_round:
                minutes += 1

        return minutes if fresh == 0 else -1


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test Case 1: [Description]
    input1 = None  # Replace with actual test input
    expected1 = None  # Replace with expected output
    result1 = solution.solve_problem(input1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print("✓ Test 1 passed")
    
    # Test Case 2: [Description]
    input2 = None  # Replace with actual test input
    expected2 = None  # Replace with expected output
    result2 = solution.solve_problem(input2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print("✓ Test 2 passed")
    
    # Test Case 3: Edge case - [Description]
    input3 = None  # Replace with edge case input
    expected3 = None  # Replace with expected output
    result3 = solution.solve_problem(input3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print("✓ Test 3 passed")
    
    print("All tests passed! ✅")


def main():
    """Main execution function"""
    print("Running solution tests...")
    test_solution()
    
    # Optional: Run with custom input
    # solution = Solution()
    # custom_input = [your_input_here]
    # result = solution.solve_problem(custom_input)
    # print(f"Result: {result}")


if __name__ == "__main__":
    main()