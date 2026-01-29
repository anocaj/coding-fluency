# Daily Coding Practice - [Problem Name]

## Problem Description

**Problem:** [Brief problem title/name]

**Source:** [LeetCode/HackerRank/etc. with problem number if applicable]

**Difficulty:** [Easy/Medium/Hard]

### Problem Statement
200. Number of Islands
Medium
Topics

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 
### Examples
Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.


## Approach/Pseudocode
dfs or bfs 


### Initial Thoughts
search for land first: if no land return 0 and mark cells visited or as water

have a counter for the number if islands
when first cell is reached -> run dfs and mark all as visited or as water. 
count up

then find new land again which was not visited: 
run dfs again

if there is no land anymore return number of islands



### Approach
this method allows to find number of islands and uses a clever way to mark visited by using the input matrix itself.
when could this break? not really since we always go down and afterwards mark it as water. therefore we visited this cell already

### Pseudocode
```
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(row,col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == "0":
                return

            grid[row][col] = "0"

            dfs(row+1,col)
            dfs(row,col+1)
            dfs(row-1,col)
            dfs(row,col-1)


        numIsland = 0
        for row in range(ROWS):
            for col in range(COLS):
                cell = grid[row][col]
                if cell == "1":
                    dfs(row,col)
                    numIsland += 1

        return numIsland
            
```

### Alternative Approaches Considered
[List any other approaches you considered and why you didn't choose them]

## Edge Cases

- [ ] **Empty input:** [How does your solution handle empty arrays, strings, etc.?]
- [ ] **Single element:** [What happens with minimal input?]
- [ ] **Maximum constraints:** [How does it perform at the upper limits?]
- [ ] **Negative numbers/Invalid input:** [How do you handle unexpected input?]
- [ ] **Duplicates:** [If applicable, how do you handle duplicate values?]
- [ ] **[Custom edge case]:** [Add problem-specific edge cases]

## Time & Space Complexity

### Time Complexity
**O([your analysis])** - [Explain why this is the time complexity]

### Space Complexity  
**O([your analysis])** - [Explain the space usage, including auxiliary space]

### Optimization Notes
[Any thoughts on how this could be optimized further, or trade-offs made]

---

**Planning completed at:** 2026-01-29 07:08:01
**Estimated implementation time:** [your estimate]