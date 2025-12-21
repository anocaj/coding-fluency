"""
Daily Coding Practice Solution
Problem: [Problem Name]
Date: 2025-12-21
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



class FileSystem:
    class Node:
        def __init__(self, isFile=False):
            self.isFile = isFile
            self.content = ""        # Only used if this node is a file.
            self.children = {}       # Dictionary of child name to Node (used if this node is a directory).
    
    def __init__(self):
        self.root =  self.Node(isFile=False)

    def ls(self, path = "/"):
        node = self._traverse(path)
        if node is None:
            return [] 
        if node.isFile:
            name = path.split("/")[-1]
            return [name]
        return sorted(node.children.keys())

    def mkdir(self, path):
        parts = [p for p in path.split("/") if p]  # ignore empty parts (leading slash)
        
        current = self.root
        for part in parts:
            if part not in current.children:
                #create new dict node of not present
                current.children[part] = self.Node(isFile=False)
            current = current.children[part]
            current.isFile = False
        
        
    def addContentToFile(self, filePath, content):
        parts = [p for p in filePath.split("/") if p]  # ignore empty parts (leading slash)
        current = self.root
        for part in parts [:-1]:
            if part not in current.children:
                current.children[part] = self.Node(isFile = False)
            current = current.children[part]
            current.isFile = False
        file_name = parts[-1]
        if file_name not in current.children:
            current.children[file_name] = self.Node(isFile=True)
        file_node = current.children[file_name]
        file_node.isFile = True

        file_node.content += content

    def readContentFromFile(self, filePath):
        node = self._traverse(filePath)
        if node is None or not node.isFile:
            return ""
        return node.content


    def _traverse(self, path:str):
        if path == "/":
            return self.root
        parts = [p for p in path.split("/") if p]
        current = self.root
        for part in parts:
            if part not in current.children:
                return None # path does not exist (in valid usage won't occur)
            current = current.children[part]
        return current
            
        



class Solution:
    def solve_problem(self, input_param):
        """
        [Brief description of what this function does]
        
        Args:
            input_param: [Description of the input parameter and its type]
            
        Returns:
            [Description of what the function returns and its type]
            
        Time Complexity: O([your analysis])
        Space Complexity: O([your analysis])
        """
        fs = FileSystem()
        print(fs.ls())
        fs.mkdir("/a/b/c")
        fs.addContentToFile("/a/b/c/d","hello")
        print(fs.ls())
        print(fs.readContentFromFile("/a/b/c/d"))

        


def test_solution():
    """Test cases for the solution"""
    solution = Solution()

    # fs = solution.FileSystem()
    
    # # Test Case 1: [Description]
    # input1 = None  # Replace with actual test input
    # expected1 = None  # Replace with expected output
    # result1 = solution.solve_problem(input1)
    # assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    # print("✓ Test 1 passed")
    
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
    
    # print("All tests passed! ✅")


def main():
    """Main execution function"""
    print("Running solution tests...")
    # test_solution()
    # solve_problem
    # Optional: Run with custom input
    solution = Solution()
    solution.solve_problem("")
    # custom_input = [your_input_here]
    # result = solution.solve_problem(custom_input)
    # print(f"Result: {result}")


if __name__ == "__main__":
    main()