# Daily Coding Practice - [Problem Name]

## Problem Description

**Problem:** Tree

**Source:** Helsing Example

**Difficulty:** Medium

### Problem Statement
1. Tree
tree is a command-line tool for pretty-printing the directory structure at the point of invocation.
```sh
$ tree
.
├── uv.lock
├── pyproject.toml
├── README.md
└── src
└── hs_interviewing_coderpad_automation
├── __init__.py
├── coderpad_client.py
├── main.py
├── model.py
├── py.typed
├── synchronizer.py
├── testing
│ ├── __init__.py
│ ├── __pycache__
│ │ ├── __init__.cpython-313.pyc
│ │ └── __init__.cpython-314.pyc
│ ├── cxx.py
│ ├── python.py
│ └── rust.py
├── utils.py
└── utils_test.py
5 directories, 17 files
```
Write a program that performs tree on a mocked file-system, printing your output in the format as
shown above.

### Examples
```sh
Input: os.listdir(path='.') ["uv.lock", "README.md", "src","testing/__init__.py"]

Output: 
.
├── uv.lock
├── README.md
├── src
├── testing
│ ├── __init__.py
5 directories, 17 files

Explanation: [brief explanation if needed]
```

## Approach/Pseudocode

### Initial Thoughts
We get a list of directories and files in currend directory. this list contains files and directories. When iterating through the list we need to check if there are files in the directories. therefore we could use an recursive approach / iterative approach.

for each iteration we track the depth of nested directories. and we need to ensure we identify the last file to close the prinint

### Approach
I choose the iterative approach since its slightly faster than recursion since it does not build the stack.


### Pseudocode
```
1. get the list with os.listdir(path='.')
2. dirCount, fileCount = 1,0
2. iterate through the listitem
    for each list item 
        print with  ├── if we are not at the end of the list
        print with └── if we are at the end of the list 
        fileCount++
        if there is a list of children
            dirCount++
            if there are no children: go to next list item 
            if there are children -> increase depth, update currentpath and run through print function.

    printfunction (depth, currItem, last):


3. print total directory count and file count
4. [Final step and return]
```

### Alternative Approaches Considered
recursive and breath first seach

## Edge Cases

- [ ] **Empty input:** empty directory => 
   .
   1 directories, 0 files
- [ ] **Single element:** 
   .
   └── file.md
   1 directories, 1 files
- [ ] **Maximum constraints:** very nested loop iterative approach better than recursive
- [ ] **Negative numbers/Invalid input:** impossible
- [ ] **Duplicates:** impossible
- [ ] **[Custom edge case]:** special characters

## Time & Space Complexity

### Time Complexity
**O([your analysis])** - [Explain why this is the time complexity]

### Space Complexity  
**O([your analysis])** - [Explain the space usage, including auxiliary space]

### Optimization Notes
[Any thoughts on how this could be optimized further, or trade-offs made]

---

**Planning completed at:** 2025-12-20 14:05:48
**Estimated implementation time:** [your estimate]