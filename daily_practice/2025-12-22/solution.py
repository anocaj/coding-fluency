"""
Daily Coding Practice Solution
Problem: Triangles
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

            print(mappedLine)

    def drawPixels(self, pixels):
        # print(pixels)
        for pixel in pixels:
            # print(pixel)
            row, col = pixel[0]
            self.screen[round(row)][round(col)] = pixel[1]

    def drawPerimeter(self,point1,point2, point3, color):
        pixels = []
        pixels.extend(self.drawLine(point1,point2, color))
        pixels.extend(self.drawLine(point1,point3, color))
        pixels.extend(self.drawLine(point3,point2 , color))
        return pixels
    def floodFill(self, point, color):
        # we only now boundaries once we reach them
        # approach would be a dfs algorithm that checks surrounding points.
        # if out of bounds reached stop
        # detect boundary?
        # we know our current color i.e. 2 
        # now we start and check surroundings:
        # if surroundings match defined color dont continue. if it does not match. mark current color and continue to the next
        # mark as visited
        visited = [[False for col in range(72)] for row in range(32)]
        target_color = self.screen[point[0]][point[1]]
        def dfs(point):
            row, col = point

            if row < 0 or row > 32 - 1 or col < 0 or col > 72 - 1 \
                    or self.screen[row][col] != target_color  or visited[row][col]:
                return
            
            self.screen[row][col] = color
            visited[row][col] = True

            # now run dfs in all directions
            dfs([point[0]+1,point[1]+0]) # Bottom
            dfs([point[0]+0,point[1]+1]) # Right
            dfs([point[0]-1,point[1]+0]) # Top
            dfs([point[0]+0,point[1]-1]) # Left

        if target_color == color:
            return  # already filled, nothing to do
        dfs(point)



    def fillTriangle(self, point1, point2, point3, color):
        perimeterPoints = self.drawPerimeter(point1, point2, point3, color)
        # print(perimeterPoints)

        # iterate through points
        # create a map for each row and store its min and max:
        minMaxMap = {}#{row: [min,max]}

        for point in perimeterPoints:
            coord = point[0]
            row = coord[0]
            col = coord[1]


            idx = round(row)
            if idx not in minMaxMap:
                minMaxMap[idx] = [min(73,col),max(-1,col)]
            else:
                minMaxMap[idx][0] = min(minMaxMap[idx][0], col)
                minMaxMap[idx][1] = max(minMaxMap[idx][1], col)


        # print(minMaxMap)
        for row in minMaxMap:
            # print(row)
            # print(minMaxMap[row][0],minMaxMap[row][1])
            self.drawLine([row,minMaxMap[row][0]],[row,minMaxMap[row][1]],color)


    def drawLine(self, point1, point2, color):
        pixels = []
        # check if out of bound if needed
        if point1[0] == point2[0] and point1[1] == point2[1]:
            pixels.append([point1,color])
            # self.drawPixels([[point1,color]])
        elif point1[0] == point2[0]: # same row 
            row = point1[0]
            for i in range(round(min(point1[1],point2[1])), round(max(point1[1],point2[1]))):
                pixels.append([[row,i],color])
                # self.drawPixels([[[row,i],color]])

        elif point1[1] == point2[1]:# same col or same row
            col = point1[1]
            for i in range(min(point1[0],point2[0]), max(point1[0],point2[0])):
                pixels.append([[i,col],color])
                # self.drawPixels([[[i,col],color]])
            
        else: # compute number of steps
            dcol = abs(point1[1]-point2[1])
            drow = abs(point1[0]-point2[0])
            steps = max(dcol,drow)

            # interpolate
            pixels = [[point1,color]]

            stepSize = [(point2[0]-point1[0])/steps, (point2[1]-point1[1])/steps]
            # print("stepSize: ",stepSize)
            
            for i in range(steps):
                lastPoint = pixels[-1]
                lastCoord = lastPoint[0]
                nextPoint = [lastCoord[0]+stepSize[0], lastCoord[1]+stepSize[1]]
                # print("nextPoint: ",nextPoint)

                pixels.append([nextPoint,color])

        self.drawPixels(pixels)
        return pixels
        

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

        point1 = [0,0]
        # point2 = [2,4]
        point2 = [31,71]
        color = 2

        triangles.drawLine(point1,point2, color)


        triangles.render()

        # triangles.drawLine([12,0],[12,70], color)
        # triangles.drawLine([12,0],[30,35], color)
        # triangles.drawLine([30,35],[12,70] , color)

        print("DRAW Triangle")

        triangles = Triangles()
        triangles.fillTriangle([12,0], [12,70], [30,35], 2)
        triangles.render()
        # what about multiple triangles in same row?


        print("DRAW Flood fill")

        triangles = Triangles()
        triangles.drawPerimeter([12,0], [12,70], [30,35], 2)
        triangles.render()

        # any point in triangle 
        pointInTriangle = [15, 35]
        triangles.floodFill(pointInTriangle, 3)
        triangles.render()


        # point outside of triangle? how to handle that? I think we want to get
        # pointOutOfTriangle = [10,2]
        # any point in triangle 
        pointInTriangle = [10,2]
        triangles.floodFill(pointInTriangle, 1)
        triangles.render()

        # what about multiple triangles? deprioritized


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