"""
Daily Coding Practice Solution
Problem: [Problem Name]
Date: 2025-12-24
"""

# Standard library imports
from typing import List, Optional, Dict, Set, Tuple, TypedDict
import collections
import heapq
import bisect

# Additional imports as needed
# import math
# import itertools
# import functools
class MoveResult(TypedDict):
    valid: bool
    winner: Optional[int]
class ConnectFour():
    def __init__(self):
        self.COLS = 7
        self.ROWS = 6
        self.grid = [[ 0 for col in range(self.COLS) ] for row in range(self.ROWS)]
        self.validPlayerIds = [1,2]
        self.curPlayer = 1 # one or two
        self.winner = None

    def drop_coin(self, player_id, column, debug = False) -> MoveResult:
        if self.winner is not None:
            return {"valid": False, "winner": self.winner}

        if column < 0 or column >= self.COLS:
            return {"valid": False, "winner": None}

        if self.grid[0][column] != 0:
            return {"valid": False, "winner": None}

        if player_id not in self.validPlayerIds:
            return {"valid": False, "winner": None}

        if player_id != self.curPlayer:
            return {"valid": False, "winner": None}

        # place coin
        for row in range(self.ROWS - 1, -1, -1):
            if self.grid[row][column] == 0:
                self.grid[row][column] = player_id
                idxRow = row
                break

        # detect win BEFORE switching player
        if debug:
            print(f"player_id: {player_id}, idxRow: {idxRow}, column: {column}")
        if self.detectWin(player_id, idxRow, column):
            self.winner = player_id
            return {"valid": True, "winner": player_id}

        self.curPlayer = self.curPlayer % 2 + 1
        return {"valid": True, "winner": None}
        
    def detectWin(self,player, row, col) -> bool:
        directions = [
            (0,1), # horizontal
            (1,0), # vertical
            (1,1), # diagonal tr -> bl
            (1,-1) # diagonal br -> tl
            ]
        for dr, dc in directions:
            count = 1

            # scan in + direction
            r,c = row + dr, col + dc
            while 0 <= r < self.ROWS and 0 <= c < self.COLS and self.grid[r][c] == player:
                count += 1
                r += dr
                c += dc
            # scan in - direction
            r,c = row - dr, col - dc
            while 0 <= r < self.ROWS and 0 <= c < self.COLS and self.grid[r][c] == player:
                count += 1
                r -= dr
                c -= dc

            if count >= 4:
                return True
            
        return False
            
    def is_draw(self) -> bool:
        # If someone already won, it's not a draw
        if self.winner is not None:
            return False

        # If any column is not full, it's not a draw
        for col in range(self.COLS):
            if self.grid[0][col] == 0:
                return False

        return True

    def printState(self):
        for row in self.grid:
            print(row)
        print("Current Player: ", self.curPlayer)



class Solution:
    def solve_problem(self, input_param):
        game = ConnectFour()
        print(game.drop_coin(1, 3))
        print(game.drop_coin(2, 3))
        print(game.drop_coin(1, 4))
        print(game.drop_coin(2, 2))
        print(game.drop_coin(1, 5))
        print(game.drop_coin(2, 1))
        print(game.drop_coin(1, 6, True)) #-> should return True
        # print(game.drop_coin(2, 0))

        game.printState()


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    solution.solve_problem(None)
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
    test_solution()
    
    # Optional: Run with custom input
    # solution = Solution()
    # custom_input = [your_input_here]
    # result = solution.solve_problem(custom_input)
    # print(f"Result: {result}")


if __name__ == "__main__":
    main()