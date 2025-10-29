"""
Daily Warm-up: Python Idioms
============================
Time: 10-15 minutes daily practice
Focus: Python-specific language features and idiomatic patterns

Instructions:
- Practice one exercise at a time
- Focus on speed and accuracy
- Repeat exercises until patterns become automatic
- Time yourself to build fluency

Usage: Run `python python_idioms.py` to execute all tests
"""

# Exercise 1: Variable Swapping Pattern
def swap_variables(a, b):
    """
    Demonstrate tuple unpacking for variable swapping.
    
    Args:
        a: First variable
        b: Second variable
    
    Returns:
        tuple: (swapped_a, swapped_b)
        
    Example:
        >>> swap_variables(1, 2)
        (2, 1)
    """
    pass

# Exercise 2: Min/Max with Defaults Pattern
def safe_min_max(arr, default_min=0, default_max=0):
    """
    Demonstrate safe min/max operations with default values.
    
    Args:
        arr: List of numbers (may be empty)
        default_min: Default value if array is empty
        default_max: Default value if array is empty
    
    Returns:
        tuple: (min_value, max_value)
        
    Example:
        >>> safe_min_max([3, 1, 4, 1, 5])
        (1, 5)
        >>> safe_min_max([], -1, -1)
        (-1, -1)
    """
    pass

# Exercise 3: Any/All Conditions Pattern
def check_conditions(arr, condition_func):
    """
    Demonstrate any() and all() for boolean aggregation.
    
    Args:
        arr: List of elements to check
        condition_func: Function that returns boolean for each element
    
    Returns:
        tuple: (any_match, all_match)
        
    Example:
        >>> check_conditions([2, 4, 6, 8], lambda x: x % 2 == 0)
        (True, True)
        >>> check_conditions([1, 2, 3], lambda x: x % 2 == 0)
        (True, False)
    """
    pass

# Exercise 4: Enumerate with Conditions Pattern
def enumerate_with_filter(arr, condition_func):
    """
    Demonstrate enumerate() combined with conditional logic.
    
    Args:
        arr: List to process
        condition_func: Function to filter elements
    
    Returns:
        list: List of (index, value) tuples for elements meeting condition
        
    Example:
        >>> enumerate_with_filter([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
        [(1, 2), (3, 4)]
    """
    pass

# Exercise 5: Generator Expression Pattern
def sum_with_generator(arr, transform_func, condition_func):
    """
    Demonstrate generator expressions for memory-efficient processing.
    
    Args:
        arr: List to process
        transform_func: Function to transform each element
        condition_func: Function to filter elements
    
    Returns:
        int: Sum of transformed elements meeting condition
        
    Example:
        >>> sum_with_generator([1, 2, 3, 4, 5], lambda x: x * 2, lambda x: x % 2 == 1)
        18
    """
    pass

# Test cases
def test_swap_variables():
    assert swap_variables(1, 2) == (2, 1)
    assert swap_variables('a', 'b') == ('b', 'a')
    assert swap_variables([1], [2]) == ([2], [1])

def test_safe_min_max():
    assert safe_min_max([3, 1, 4, 1, 5]) == (1, 5)
    assert safe_min_max([], -1, -1) == (-1, -1)
    assert safe_min_max([42]) == (42, 42)

def test_check_conditions():
    assert check_conditions([2, 4, 6, 8], lambda x: x % 2 == 0) == (True, True)
    assert check_conditions([1, 2, 3], lambda x: x % 2 == 0) == (True, False)
    assert check_conditions([1, 3, 5], lambda x: x % 2 == 0) == (False, False)

def test_enumerate_with_filter():
    result = enumerate_with_filter([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
    assert result == [(1, 2), (3, 4)]
    assert enumerate_with_filter([1, 3, 5], lambda x: x % 2 == 0) == []

def test_sum_with_generator():
    result = sum_with_generator([1, 2, 3, 4, 5], lambda x: x * 2, lambda x: x % 2 == 1)
    assert result == 18  # (1*2) + (3*2) + (5*2) = 2 + 6 + 10 = 18
    assert sum_with_generator([], lambda x: x, lambda x: True) == 0

if __name__ == "__main__":
    test_swap_variables()
    test_safe_min_max()
    test_check_conditions()
    test_enumerate_with_filter()
    test_sum_with_generator()
    print("All Python idiom pattern tests passed!")