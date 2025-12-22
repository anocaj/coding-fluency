# Daily Coding Practice - [Problem Name]

## Problem Description

**Problem:** Terminal Graphics (Triangles)

**Source:** Helsing Interview

**Difficulty:** Hard

### Problem Statement
Simulate a 32×72 screen of pixels; implement line drawing, triangle edges/fill and flood-fill.

2. Triangles
six steps.
For this problem, you will be rendering various graphics primitives to the terminal, working through
Note that you can render the following pixels to the terminal by printing the following:
• Yellow pixel: \\x1b[43m \\x1b[0m
• Blue pixel: \\x1b[44m \\x1b[0m
• Black pixel: \\x1b[40m \\x1b[0m
(This is true for most languages. If you are using Java, Scala, or Clojure, change the escape
character to \\u001B[. If you are using Ruby, change the escape character to \\e[.)
Step 1: Create a data structure representing a screen, which will be of size 32 (rows) × 72 (columns),
each entry storing a pixel that can be yellow, black or blue. Write a function that renders it to the
terminal.
Step 2: Next, write functionality that takes the previously created screen data structure and a
collection of pixels (each containing a row and column coordinate, and a colour), and updates the
screen with these pixels drawn accordingly.
Step 3: Now that you can draw pixels on a screen, let’s create some lines using a pre-set
algorithm. Write functionality that takes two sets of coordinates: one for the starting point, point1,
and one for the ending point, point2, and the colour of this line and generates all the pixels
corresponding to the line.
The algorithm for generating the lines is as follows:
• If the starting and ending points are the same, then the line is just a single pixel, otherwise…
• Compute the number of steps the algorithm will take.
‣ To do this, first compute dcolumn = |point1.column - point2.column| and drow = |point1.row -
point2.row|.
‣ Then, the steps is defined as max(dcolumn, drow).
• “Interpolate” steps times between the start and end point, round each set of points to the
nearest pixel to produce all of the points of the line.
‣ Start with the point point1.
‣ Generate the next point by adding (point2.row - point1.row) / steps to the row and
(point2.column - point1.column) / steps to the column.
‣ Repeat the previous step steps times to get all the points needed for the line.
Step 4: Having unlocked lines, now draw the perimeter of a triangle.
Step 5: Now that you can render the perimeters of triangles, implement a filled triangle using the
scanline algorithm:
• Generate the collection of points representing the perimeter of the triangle.
• For each row of the triangle, determine the minimum and maximum column coordinates for that
row. Draw a line from (row, min_column) to (row, max_column).
Step 6: Finally, implement flood filling functionality. Specify a coordinate inside your screen along
with a colour, and fill in all (transitively) adjacent (up, down, left, right) pixels of the same colour with
the new colour.
### Examples
```
Input: [example input]
Output: [example output]
Explanation: [brief explanation if needed]
```

## Approach/Pseudocode

### Initial Thoughts
create data structure matrix[32][72].
each cell is a pixel containing a color either(yellow,black, blue) or emtpy 
have a hashmap to map colors to ascii code: 
colorMap: {
    0: " ", empty
    1: "\\x1b[43m \\x1b[0m",# yellow
    2: "\\x1b[40m \\x1b[0m", # black
    3: "\\\x1b[44m \\x1b[0m", # blue
}

how are these characters being drawn? do they have the same letterspace? lets check this 

further we want  a function that renders the screen to terminal:
def render():
    for line in screen:
        mappedLine = []
        for char in screen[line]:
            mappedLine.append(colorMap[char])

        print(f"{mappedLine.join()}/n")
    

Step 2:

pixels = [
    {coord: [row,col], color: 1|2|3}
]
def drawPixels(pixels):
    # apply pixels to screen
        for pixel in pixels:
            row, col = pixel.coord
            self.screen[row][col] = pixel.color
    
    
# step 3
draw Line
def drawLine(point1=[row,col], point2=[row,col], color=0|1|2):
    # check if out of bound if needed
    if point1[0] == point2[0] and point1[1] == point2[1]:
        drawPixel([point1])
    elif point1[0] == point2[0]: # same row 
        # generate pixels
        for from min(point1[1],point2[1]) to max(point1[1],point2[1])

    elif point1[1] == point2[1]# same col or same row:
        # generate pixels
        for from min(point1[0],point2[0]) to max(point1[0],point2[0])
        
    else: # compute number of steps
        dcol = abs(point1[1]-point2[1])
        drow = abs(point1[0]-point2[0])
        steps = max(dcol,drow)

        # interpolate
        pixels = [point1]
        for i in range(steps):
            nextPoint = [pixels[i][0]+point2[0]-point1[0]/steps, pixels[i][1]+point2[1]-point1[1]/steps]
            pixels.append(nextPoint)





#
  0,1,2,3,4,5,6,7
0 d  
1      
2        .
3
4
5

dcol = 2-0 = 2
drow = 4-0 = 4
steps = max(2,4) = 4
curr point = draw [0,0]
curr point = next point = ["2/4",1] = [0+0,0+1] 
draw [0,1]
urr point = ["1/4",1]  = [0,1]=  [0+0,1+1] 


### Approach
[Describe your chosen approach in plain English. Why did you choose this method?]

### Pseudocode
```
1. [Step 1 of your algorithm]
2. [Step 2 of your algorithm]
3. [Continue with logical steps...]
4. [Final step and return]
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

**Planning completed at:** 2025-12-22 09:51:11
**Estimated implementation time:** [your estimate]