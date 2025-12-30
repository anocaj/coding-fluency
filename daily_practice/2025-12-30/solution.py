"""
Daily Coding Practice Solution
Problem: [Problem Name]
Date: 2025-12-30
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
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        dependencies = collections.defaultdict(list) # dependent node -> in
        indegree = collections.defaultdict(int)
        all_nodes = set()
        result = []

        for edge in prerequisites:
            source = edge[1]
            target = edge[0]
            all_nodes.add(source)
            all_nodes.add(target)

            dependencies[source].append(target)
            indegree[target] += 1

        queue = collections.deque()
        hasindegree0 = False
        for node in all_nodes:
            if indegree[node] == 0:
                hasindegree0 = True
                queue.append(node)
        if hasindegree0 == False:
            return False
            
                
        while queue:
            node = queue.popleft()
            result.append(source)
        
            for target in dependencies[source]:
                if indegree[target] == 0:
                    queue.append(target)
                indegree[target] -= 1

        print(result)
        return True if len(result) != numCourses  else False

def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test Case 1: [Description]
    expected1 = True  # Replace with expected output
    result1 = solution.canFinish(2, [[1,0]]
)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print("✓ Test 1 passed")
    
    # Test Case 2: [Description]
    # input2 = None  # Replace with actual test input
    expected2 = False  # Replace with expected output
    result2 = solution.canFinish(2,[[1,0],[0,1]] )
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print("✓ Test 2 passed")
    
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