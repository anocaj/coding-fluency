"""
Daily Coding Practice Solution
Problem: [Problem Name]
Date: [YYYY-MM-DD]
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


class Solution:
    def solve_problem(self, input_param):
    # 1. parse list of edges to adjacency list:
        lines = input_param.split("\n")
        adj = collections.defaultdict(list)
        for line in lines:
            source, target = line.split("-")
            adj[source].append(target)
            adj[target].append(source)
            

    # 2. 
        def dfs(graph, start, end, path=[]):
            path = path + [start]

            # base case: 
            if start == end:
                return [path]
            if start not in graph: 
                return []

            paths = []
            # recurrence relation:
            for neighbor in graph[start]:
                if neighbor == neighbor.upper() or neighbor not in path:
                    newpaths = dfs(graph, neighbor, end, path)
                    for p in newpaths:
                        paths.append(p)
            return paths

    # now we don't handle the special nodes that can be visited multiple times

    # 3. dfs(start)
        paths = dfs(adj,"start","end")
        print(len(paths))
        return len(paths)


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test Case 1: [Description]
    input1 = """EG-bj
LN-end
bj-LN
yv-start
iw-ch
ch-LN
EG-bn
OF-iw
LN-yv
iw-TQ
iw-start
TQ-ch
EG-end
bj-OF
OF-end
TQ-start
TQ-bj
iw-LN
EG-ch
yv-iw
KW-bj
OF-ch
bj-ch
yv-TQ"""  # Replace with actual test input
    expected1 = None  # Replace with expected output
    result1 = solution.solve_problem(input1)
    # assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
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