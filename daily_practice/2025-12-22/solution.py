"""
Daily Coding Practice Solution
Problem: [Problem Name]
Date: 2025-12-22
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

class Triangles:
    def __init__(self):
        # self.screen = [[1] * 72] * 32 # this causes an error which effects all columns when updating only a single coordinate
        self.screen = [[1 for col in range(72)] for row in range(32)]
        self.colorMap =    { 
            # 0: " ", #empty
            1: "\x1b[43m \x1b[0m",# yellow
            2: "\x1b[40m \x1b[0m", # black
            3: "\x1b[44m \x1b[0m", # blue
        }

    def render(self):
        ROWS, COLS = len(self.screen), len(self.screen[0])
        for row in range(ROWS):
            mappedLine = ""
            for col in range(COLS):
                pixel = self.screen[row][col]
                mappedLine = mappedLine + self.colorMap[pixel]

            print(f"{mappedLine}")

    def drawPixels(self, pixels):
        print(pixels)
        for pixel in pixels:
            print(pixel)
            row, col = pixel[0]
            self.screen[round(row)][round(col)] = pixel[1]

    def drawLine(self, point1, point2, color):
        # check if out of bound if needed
        if point1[0] == point2[0] and point1[1] == point2[1]:
            self.drawPixels([[point1,color]])
        elif point1[0] == point2[0]: # same row 
            row = point1[0]
            for i in range(min(point1[1],point2[1]), max(point1[1],point2[1])):
                self.drawPixels([[[row,i],color]])

        elif point1[1] == point2[1]:# same col or same row
            col = point1[1]
            for i in range(min(point1[0],point2[0]), max(point1[0],point2[0])):
                self.drawPixels([[[i,col],color]])
            
        else: # compute number of steps
            dcol = abs(point1[1]-point2[1])
            drow = abs(point1[0]-point2[0])
            steps = max(dcol,drow)

            # interpolate
            pixels = [[point1,color]]

            stepSize = [(point2[0]-point1[0])/steps, (point2[1]-point1[1])/steps]
            print("stepSize: ",stepSize)
            
            for i in range(steps):
                lastPoint = pixels[-1]
                lastCoord = lastPoint[0]
                nextPoint = [lastCoord[0]+stepSize[0], lastCoord[1]+stepSize[1]]
                print("nextPoint: ",nextPoint)

                pixels.append([nextPoint,color])
            self.drawPixels(pixels)
        

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
        triangles = Triangles()

        triangles.render()

        # pixels = [
        #     {"coord": [1,1], "color": 2},
        #     {"coord": [3,60], "color": 3},
        #     {"coord": [31,2], "color": 2},
        #     {"coord": [31,71], "color": 3},

        #     ]
        pixels = [
            [[1,1], 2],
            [[3,60], 3],
            [[31,2], 2],
            [[31,71], 3],
            ]
        triangles.drawPixels(pixels=pixels)
        print("DRAW PIXELS")
        triangles.render()

        triangles = Triangles()

        print("DRAW LINE")

        # point1 = [0,0]
        # # point2 = [2,4]
        # point2 = [0,4]
        # color = 2

        # triangles.drawLine(point1,point2, color)

        point1 = [0,0]
        point2 = [2,4]
        # point2 = [0,4]
        color = 3

        triangles.drawLine(point1,point2, color)
        triangles.drawLine([0,10],[5,10], 2)
        triangles.drawLine([10,10],[10,15], color)

        triangles.drawLine([12,0],[12,70], color)
        triangles.drawLine([12,0],[30,35], color)
        triangles.drawLine([30,35],[12,70] , color)

        triangles.render()


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test Case 1: [Description]
    input1 = None  # Replace with actual test input
    expected1 = None  # Replace with expected output
    result1 = solution.solve_problem(input1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print("✓ Test 1 passed")
    
    
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