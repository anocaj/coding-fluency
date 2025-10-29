"""
Daily Warm-up: Loop Patterns
============================
Time: 10-15 minutes daily practice
Focus: Iteration and looping techniques for building muscle memory

Instructions:
- Practice one exercise at a time
- Focus on speed and accuracy with common iteration patterns
- Repeat exercises until patterns become automatic
- Time yourself to build fluency with different loop approaches

Usage: Run `python loop_patterns.py` to execute all tests
"""

# Exercise 1: Index Iteration Pattern
def index_iteration_exercise(arr):
    """
    Practice iterating over array indices using range(len(arr)) pattern.
    This pattern is useful when you need the index for calculations or comparisons.
    
    Args:
        arr: List of elements to iterate over
    
    Returns:
        list: New list with elements at even indices doubled
        
    Example:
        >>> index_iteration_exercise([1, 2, 3, 4, 5])
        [2, 2, 6, 4, 10]
    """
    result = []
    for i in range(len(arr)):
        if i % 2 == 0:  # Even index
            result.append(arr[i] * 2)
        else:  # Odd index
            result.append(arr[i])
    return result

# Exercise 2: Enumerate Iteration Pattern  
def enumerate_iteration_exercise(arr):
    """
    Practice using enumerate() to get both index and value in loops.
    This pattern is cleaner than manual index tracking.
    
    Args:
        arr: List of elements to process
    
    Returns:
        list: List of tuples (index, element) for elements at odd indices
        
    Example:
        >>> enumerate_iteration_exercise(['a', 'b', 'c', 'd', 'e'])
        [(1, 'b'), (3, 'd')]
    """
    result = []
    for i, element in enumerate(arr):
        if i % 2 == 1:  # Odd index
            result.append((i, element))
    return result

# Exercise 3: Reverse Iteration Pattern
def reverse_iteration_exercise(arr):
    """
    Practice iterating backwards using reversed() and negative indexing.
    Useful for algorithms that need to process elements from end to start.
    
    Args:
        arr: List of numbers to process
    
    Returns:
        list: Cumulative sum calculated from right to left
        
    Example:
        >>> reverse_iteration_exercise([1, 2, 3, 4])
        [10, 9, 7, 4]
    """
    if not arr:
        return []
    
    result = [0] * len(arr)
    cumulative_sum = 0
    
    # Iterate backwards using reversed() and enumerate
    for i, num in enumerate(reversed(arr)):
        cumulative_sum += num
        result[len(arr) - 1 - i] = cumulative_sum
    
    return result

# Exercise 4: Multiple Array Iteration Pattern
def multiple_array_iteration_exercise(arr1, arr2):
    """
    Practice using zip() to iterate over multiple arrays simultaneously.
    Essential pattern for parallel processing of related data.
    
    Args:
        arr1: First list of numbers
        arr2: Second list of numbers
    
    Returns:
        list: Element-wise sum of the two arrays
        
    Example:
        >>> multiple_array_iteration_exercise([1, 2, 3], [4, 5, 6])
        [5, 7, 9]
    """
    result = []
    for num1, num2 in zip(arr1, arr2):
        result.append(num1 + num2)
    return result

# Test cases for Exercise 1
def test_index_iteration():
    assert index_iteration_exercise([1, 2, 3, 4, 5]) == [2, 2, 6, 4, 10]
    assert index_iteration_exercise([10, 20]) == [20, 20]
    assert index_iteration_exercise([]) == []

# Test cases for Exercise 2
def test_enumerate_iteration():
    assert enumerate_iteration_exercise(['a', 'b', 'c', 'd', 'e']) == [(1, 'b'), (3, 'd')]
    assert enumerate_iteration_exercise(['x', 'y']) == [(1, 'y')]
    assert enumerate_iteration_exercise(['z']) == []

# Test cases for Exercise 3
def test_reverse_iteration():
    assert reverse_iteration_exercise([1, 2, 3, 4]) == [10, 9, 7, 4]
    assert reverse_iteration_exercise([5, 10]) == [15, 10]
    assert reverse_iteration_exercise([7]) == [7]

# Test cases for Exercise 4
def test_multiple_array_iteration():
    assert multiple_array_iteration_exercise([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
    assert multiple_array_iteration_exercise([10, 20], [5, 15]) == [15, 35]
    assert multiple_array_iteration_exercise([], []) == []

if __name__ == "__main__":
    # Run all tests
    test_index_iteration()
    test_enumerate_iteration()
    test_reverse_iteration()
    test_multiple_array_iteration()
    print("All tests passed!")