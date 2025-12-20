"""
Daily Coding Practice Solution
Problem: [Problem Name]
Date: 2025-12-20
"""

# Standard library imports
from typing import List, Optional, Dict, Set, Tuple
import collections
import heapq
import bisect

# Additional imports as needed
# import math
# import itertools
# import functools
import os

fs = {
    "uv.lock": None,
    "pyproject.toml": None,
    "README.md": None,
    "src": {
        "hs_interviewing_coderpad_automation": {
            "__init__.py": None,
            "coderpad_client.py": None,
            "main.py": None,
            "model.py": None,
            "py.typed": None,
            "synchronizer.py": None,
            "testing": {
                "__init__.py": None,
                "__pycache__": {
                    "__init__.cpython-313.pyc": None,
                    "__init__.cpython-314.pyc": None,
                },
                "cxx.py": None,
                "python.py": None,
                "rust.py": None,
            },
            "utils.py": None,
            "utils_test.py": None,
        }
    }
}

class Solution:

    def solve_problem(self, input_param):
        """
        Pretty-print a mocked file system in `tree` format.

        Args:
            fs (dict): Mocked filesystem where
                       - keys are file/directory names
                       - values are None (file) or dict (directory)

        Time Complexity: O(N)
        Space Complexity: O(D)
        """
        print(".")
        dir_count = 1 # root
        file_count = 0

        def dfs(node:dict,prefix: str):
            nonlocal dir_count, file_count

            entries = list(node.items())
            for i, (name,child) in enumerate(entries):
                is_last = i == len(entries) - 1
                connector = "└── " if is_last else "├── "

                print (prefix + connector + name)

                if child is None:
                    file_count += 1
                else:
                    dir_count += 1
                    extension = "    " if is_last else "│   "
                    dfs(child,prefix + extension)

        dfs(fs,"")
        print(f"\n{dir_count} directories, {file_count} files")


        



def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test Case 1: [Description]
    input1 = None  # Replace with actual test input
    expected1 = None  # Replace with expected output
    result1 = solution.solve_problem(input1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print("✓ Test 1 passed")
    
    # # Test Case 2: [Description]
    # input2 = None  # Replace with actual test input
    # expected2 = None  # Replace with expected output
    # result2 = solution.solve_problem(input2)
    # assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    # print("✓ Test 2 passed")
    
    # # Test Case 3: Edge case - [Description]
    # input3 = None  # Replace with edge case input
    # expected3 = None  # Replace with expected output
    # result3 = solution.solve_problem(input3)
    # assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    # print("✓ Test 3 passed")
    
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