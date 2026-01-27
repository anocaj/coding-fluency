"""
Daily Coding Practice Solution
Problem: [Problem Name]
Date: 2025-01-27
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
    def solve_problem(self, beginWord, endWord, wordList):
        def buildPatterns(wordList):
            patterns = collections.defaultdict(list)

            for word in wordList:
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    patterns[pattern].append(word)

            return patterns    
        
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        patterns = buildPatterns(wordList)

        queue = collections.deque([(beginWord,1)]) 
        visited = set([beginWord])

        while queue:
            word,steps = queue.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]

                for neighbor in patterns[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor,steps+1))

                patterns[pattern] = []

        return 0

# def test_solution():
#     """Test cases for the solution"""
#     solution = Solution()
    
#     # Test Case 1: [Description]
#     input1 = None  # Replace with actual test input
#     expected1 = None  # Replace with expected output
#     result1 = solution.solve_problem(input1)
#     assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
#     print("✓ Test 1 passed")
    
#     # Test Case 2: [Description]
#     input2 = None  # Replace with actual test input
#     expected2 = None  # Replace with expected output
#     result2 = solution.solve_problem(input2)
#     assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
#     print("✓ Test 2 passed")
    
#     # Test Case 3: Edge case - [Description]
#     input3 = None  # Replace with edge case input
#     expected3 = None  # Replace with expected output
#     result3 = solution.solve_problem(input3)
#     assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
#     print("✓ Test 3 passed")
    
#     print("All tests passed! ✅")


def main():
    """Main execution function"""
    print("Running solution tests...")
    # test_solution()
    
    # Optional: Run with custom input
    solution = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    # custom_input = [your_input_here]
    result = solution.solve_problem(beginWord, endWord, wordList)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()