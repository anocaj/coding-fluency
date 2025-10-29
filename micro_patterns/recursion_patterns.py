"""
Daily Warm-up: Recursion Patterns
=================================
Time: 10-15 minutes daily practice
Focus: Recursive thinking and memoization concepts

Instructions:
- Practice one exercise at a time
- Focus on speed and accuracy
- Repeat exercises until patterns become automatic
- Time yourself to build fluency

Usage: Run `python recursion_patterns.py` to execute all tests
"""

# Exercise 1: Base Case and Recursive Call Template Pattern
def recursive_sum(arr):
    """
    Demonstrate standard recursion structure with base cases.
    
    Args:
        arr: List of numbers to sum recursively
    
    Returns:
        int: Sum of all numbers in the array
        
    Example:
        >>> recursive_sum([1, 2, 3, 4])
        10
    """
    pass

# Exercise 2: Factorial with Base Case Pattern
def factorial_recursive(n):
    """
    Demonstrate classic factorial recursion with proper base case.
    
    Args:
        n: Non-negative integer
    
    Returns:
        int: Factorial of n
        
    Example:
        >>> factorial_recursive(5)
        120
    """
    pass

# Exercise 3: Memoization Pattern
def fibonacci_memoized(n, memo=None):
    """
    Demonstrate dictionary-based caching for recursive functions.
    
    Args:
        n: Position in fibonacci sequence
        memo: Dictionary for memoization (optional)
    
    Returns:
        int: nth fibonacci number
        
    Example:
        >>> fibonacci_memoized(10)
        55
    """
    pass

# Exercise 4: List Processing Recursion Pattern
def recursive_list_processing(arr, operation_func):
    """
    Demonstrate recursive processing of list elements.
    
    Args:
        arr: List to process recursively
        operation_func: Function to apply to each element
    
    Returns:
        list: Processed list
        
    Example:
        >>> recursive_list_processing([1, 2, 3], lambda x: x * 2)
        [2, 4, 6]
    """
    pass

# Test cases
def test_recursive_sum():
    assert recursive_sum([1, 2, 3, 4]) == 10
    assert recursive_sum([]) == 0
    assert recursive_sum([5]) == 5
    assert recursive_sum([-1, 1, -2, 2]) == 0

def test_factorial_recursive():
    assert factorial_recursive(5) == 120
    assert factorial_recursive(0) == 1
    assert factorial_recursive(1) == 1
    assert factorial_recursive(3) == 6

def test_fibonacci_memoized():
    assert fibonacci_memoized(10) == 55
    assert fibonacci_memoized(0) == 0
    assert fibonacci_memoized(1) == 1
    assert fibonacci_memoized(7) == 13

def test_recursive_list_processing():
    result = recursive_list_processing([1, 2, 3], lambda x: x * 2)
    assert result == [2, 4, 6]
    assert recursive_list_processing([], lambda x: x) == []
    assert recursive_list_processing([5], lambda x: x + 1) == [6]

if __name__ == "__main__":
    test_recursive_sum()
    test_factorial_recursive()
    test_fibonacci_memoized()
    test_recursive_list_processing()
    print("All recursion pattern tests passed!")