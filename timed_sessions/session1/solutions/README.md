# Solutions Directory

## Overview

This directory is where you'll implement your solutions during the timed session. Keep your code organized and well-documented for easy review.

## File Naming Conventions

Use the following naming pattern for your solution files:

### For Individual Problems
- `problem_e1_two_sum.py` - Easy Problem 1: Two Sum
- `problem_e2_valid_parentheses.py` - Easy Problem 2: Valid Parentheses  
- `problem_e3_merge_sorted_lists.py` - Easy Problem 3: Merge Two Sorted Lists
- `problem_m1_add_two_numbers.py` - Medium Problem 1: Add Two Numbers
- `problem_m2_longest_substring.py` - Medium Problem 2: Longest Substring Without Repeating Characters
- `problem_m3_group_anagrams.py` - Medium Problem 3: Group Anagrams
- `problem_h1_median_sorted_arrays.py` - Hard Problem 1: Median of Two Sorted Arrays
- `problem_h2_trapping_rain_water.py` - Hard Problem 2: Trapping Rain Water

### File Structure Template

Each solution file should follow this structure:

```python
"""
Problem: [Problem Name]
Difficulty: [Easy/Medium/Hard]
Time Estimate: [X minutes]
Actual Time: [X minutes] # Fill this in after completion

Description:
[Brief problem description]

Approach:
[Your approach explanation]
"""

def solution_function(parameters):
    """
    [Function description]
    
    Args:
        [parameter descriptions]
    
    Returns:
        [return value description]
    
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
    # Your implementation here
    pass

def test_solution():
    """Test cases for the solution"""
    # Test case 1
    assert solution_function(test_input_1) == expected_output_1
    
    # Test case 2  
    assert solution_function(test_input_2) == expected_output_2
    
    # Add more test cases as needed
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()
```

## Organization Guidelines

### During the Session
1. **Create files as you go** - Don't pre-create all files
2. **One problem per file** - Keep solutions separate for clarity
3. **Use descriptive names** - Follow the naming convention above
4. **Include timing notes** - Track actual vs estimated time

### Code Quality Standards
- **Clear variable names** - Use descriptive, readable names
- **Proper indentation** - Follow Python PEP 8 standards
- **Inline comments** - Explain complex logic or algorithms
- **Function docstrings** - Document parameters and return values
- **Test cases** - Include at least the provided examples

### Time Management Tips
- **Start simple** - Get a working solution first
- **Optimize later** - Don't over-engineer initially  
- **Test frequently** - Run test cases as you develop
- **Move on if stuck** - Don't spend too long on one problem

## Post-Session Review

After completing the session, use this directory to:
- Review your solutions for correctness
- Analyze time and space complexity
- Identify areas for improvement
- Compare with optimal solutions
- Note patterns and techniques used

## Example File Structure After Session

```
solutions/
├── README.md (this file)
├── problem_e1_two_sum.py
├── problem_m2_longest_substring.py
└── problem_h1_median_sorted_arrays.py
```

## Common Patterns to Remember

- **Two Pointers**: For array/string problems
- **Hash Maps**: For lookups and counting
- **Stack**: For parentheses, parsing, DFS
- **Queue**: For BFS, level-order traversal
- **Sliding Window**: For substring/subarray problems
- **Binary Search**: For sorted array problems
- **Dynamic Programming**: For optimization problems

Good luck with your session!