"""
Daily Coding Practice Solution
Problem: [Problem Name]
Date: 2025-12-29
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
    def solve_problem(self, input_param) -> List:
        """
        [Brief description of what this function does]
        
        Args:
            input_param: 
            
        Returns:
            Order of Tasks
            
        Time Complexity: O([your analysis])
        Space Complexity: O([your analysis])
        """
        # adjacency List from input: 
        # def getAdj(input)->Dict:
        graph = collections.defaultdict(list)     # dependency -> [tasks]
        indegree = collections.defaultdict(int)   # task -> number of prerequisites
        all_tasks = set()

        # Parse input
        for line in input_param.strip().split("\n"):
            parts = line.split()
            task = parts[0]
            deps = parts[1:]

            all_tasks.add(task)

            for dep in deps:
                graph[dep].append(task)
                indegree[task] += 1
                all_tasks.add(dep)

                # Initialize queue with tasks having no prerequisites
        queue = collections.deque([task for task in all_tasks if indegree[task] == 0])

        result = []

        while queue:
            current = queue.popleft()
            result.append(current)

            for neighbor in graph[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Cycle detection
        if len(result) != len(all_tasks):
            print(f"Result Length: {len(result)}")
            print(f"All Task Length: {len(all_tasks)}")
            raise ValueError("No valid task order exists (cycle detected)")

        return result


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test Case 1: [Description]
    input1 = """bake_vegetables chop_vegetables preheat_oven
chop_vegetables wash_vegetables
panfry_protein prepare_protein
clean_kitchen arrange_on_plate
prepare_protein
preheat_oven
serve_dish arrange_on_plate
wash_vegetables
arrange_on_plate bake_vegetables panfry_protein"""

    expected1 = ["prepare_protein", "preheat_oven", "wash_vegetables", "panfry_protein", "bake_vegetables", "chop_vegetables", "bake_vegetables", "arrange_on_plate", "clean_kitchen", "serve_dish"]  # Replace with expected output
    result1 = solution.solve_problem(input1)
    print(result1)
    # assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print("✓ Test 1 passed")
    
    # Test Case 2: [Description]
    input2 = """bake_vegetables chop_vegetables preheat_oven
chop_vegetables wash_vegetables
panfry_protein prepare_protein arrange_on_plate
clean_kitchen arrange_on_plate
prepare_protein
preheat_oven
serve_dish arrange_on_plate
wash_vegetables
arrange_on_plate bake_vegetables panfry_protein"""  # Replace with actual test input
    # expected2 = None  # Replace with expected output
    result2 = solution.solve_problem(input2)
    # assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print("✓ Test 2 passed")
    
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