"""
Daily Warm-up: List and String Manipulation Patterns
===================================================
Time: 10-15 minutes daily practice
Focus: Data structure manipulation and transformation patterns

Instructions:
- Practice one exercise at a time
- Focus on speed and accuracy with slicing, comprehensions, and string operations
- Repeat exercises until patterns become automatic
- Time yourself to build fluency with data manipulation

Usage: Run `python list_string_patterns.py` to execute all tests
"""


# Exercise 1: List Reversal Patterns
def reverse_list_patterns(arr):
    """
    Demonstrate different methods for reversing lists and their use cases.
    
    Args:
        arr: List to reverse
    
    Returns:
        tuple: (sliced_reverse, reversed_list, original_list)
        
    Example:
        >>> reverse_list_patterns([1, 2, 3, 4])
        ([4, 3, 2, 1], [4, 3, 2, 1], [1, 2, 3, 4])
    """
    # Method 1: Slicing with [::-1] - creates new list
    sliced_reverse = arr[::-1]
    
    # Method 2: Using reversed() function - creates new list
    reversed_list = list(reversed(arr))
    
    # Original list remains unchanged
    original_list = arr.copy()
    
    return (sliced_reverse, reversed_list, original_list)


# Exercise 2: Subarray Slicing Operations
def subarray_slicing_patterns(arr, start, end, step=1):
    """
    Demonstrate slice notation patterns for extracting subarrays.
    
    Args:
        arr: List to slice
        start: Starting index
        end: Ending index (exclusive)
        step: Step size for slicing
    
    Returns:
        dict: Various slicing operations and their results
        
    Example:
        >>> subarray_slicing_patterns([0, 1, 2, 3, 4, 5], 1, 4)
        {'basic_slice': [1, 2, 3], 'with_step': [1, 3], 'reverse_slice': [3, 2, 1]}
    """
    # Basic slice notation [start:end]
    basic_slice = arr[start:end:step]
    
    # Slice with step=2 from the basic range
    with_step = arr[start:end:2]
    
    # Reverse the sliced portion
    reverse_slice = arr[start:end][::-1]
    
    return {
        'basic_slice': basic_slice,
        'with_step': with_step,
        'reverse_slice': reverse_slice
    }


# Exercise 3: List Comprehension Filtering
def list_comprehension_filtering(data, condition_func):
    """
    Demonstrate filtering and transformation using list comprehensions.
    
    Args:
        data: List of items to filter/transform
        condition_func: Function that returns True for items to keep
    
    Returns:
        dict: Results of different comprehension patterns
        
    Example:
        >>> list_comprehension_filtering([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
        {'filtered': [2, 4], 'squared_evens': [4, 16], 'conditional_transform': [1, 4, 3, 16, 5]}
    """
    # Basic filtering with list comprehension
    filtered = [x for x in data if condition_func(x)]
    
    # Transform filtered items (square the even numbers)
    squared_evens = [x * x for x in data if condition_func(x)]
    
    # Conditional transformation (square if condition met, otherwise keep original)
    conditional_transform = [x * x if condition_func(x) else x for x in data]
    
    return {
        'filtered': filtered,
        'squared_evens': squared_evens,
        'conditional_transform': conditional_transform
    }


# Exercise 4: String Join and Split Operations
def string_join_split_patterns(text, delimiter):
    """
    Demonstrate string manipulation using join() and split() methods.
    
    Args:
        text: String to manipulate
        delimiter: Character(s) to use for splitting/joining
    
    Returns:
        dict: Results of various string operations
        
    Example:
        >>> string_join_split_patterns("hello,world,python", ",")
        {'split_result': ['hello', 'world', 'python'], 'rejoined': 'hello,world,python', 'transformed': 'HELLO-WORLD-PYTHON'}
    """
    # Split string into list using delimiter
    split_result = text.split(delimiter)
    
    # Rejoin the split parts with same delimiter
    rejoined = delimiter.join(split_result)
    
    # Transform: uppercase and join with different delimiter
    transformed = "-".join(word.upper() for word in split_result)
    
    return {
        'split_result': split_result,
        'rejoined': rejoined,
        'transformed': transformed
    }


# Exercise 5: List Flattening and Nested Operations
def nested_list_patterns(nested_data):
    """
    Demonstrate flattening nested lists and working with nested structures.
    
    Args:
        nested_data: List containing nested lists
    
    Returns:
        dict: Results of flattening and nested operations
        
    Example:
        >>> nested_list_patterns([[1, 2], [3, 4], [5]])
        {'flattened': [1, 2, 3, 4, 5], 'lengths': [2, 2, 1], 'max_in_each': [2, 4, 5]}
    """
    # Flatten nested list using list comprehension
    flattened = [item for sublist in nested_data for item in sublist]
    
    # Get length of each nested list
    lengths = [len(sublist) for sublist in nested_data]
    
    # Get maximum value in each non-empty nested list
    max_in_each = [max(sublist) for sublist in nested_data if sublist]
    
    return {
        'flattened': flattened,
        'lengths': lengths,
        'max_in_each': max_in_each
    }


# Test cases for Exercise 1
def test_reverse_list_patterns():
    result = reverse_list_patterns([1, 2, 3, 4])
    assert result[0] == [4, 3, 2, 1]  # sliced reverse
    assert result[1] == [4, 3, 2, 1]  # reversed() result
    assert result[2] == [1, 2, 3, 4]  # original unchanged
    
    # Test with empty list
    empty_result = reverse_list_patterns([])
    assert empty_result[0] == []
    assert empty_result[1] == []
    assert empty_result[2] == []


# Test cases for Exercise 2
def test_subarray_slicing_patterns():
    result = subarray_slicing_patterns([0, 1, 2, 3, 4, 5], 1, 4)
    assert result['basic_slice'] == [1, 2, 3]
    assert result['with_step'] == [1, 3]
    assert result['reverse_slice'] == [3, 2, 1]
    
    # Test with step parameter
    result_step = subarray_slicing_patterns([0, 1, 2, 3, 4, 5], 0, 6, 2)
    assert result_step['basic_slice'] == [0, 2, 4]  # Fixed: step=2 means every 2nd element


# Test cases for Exercise 3
def test_list_comprehension_filtering():
    result = list_comprehension_filtering([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
    assert result['filtered'] == [2, 4]
    assert result['squared_evens'] == [4, 16]
    assert result['conditional_transform'] == [1, 4, 3, 16, 5]
    
    # Test with all odd numbers
    odd_result = list_comprehension_filtering([1, 3, 5], lambda x: x % 2 == 0)
    assert odd_result['filtered'] == []


# Test cases for Exercise 4
def test_string_join_split_patterns():
    result = string_join_split_patterns("hello,world,python", ",")
    assert result['split_result'] == ['hello', 'world', 'python']
    assert result['rejoined'] == 'hello,world,python'
    assert result['transformed'] == 'HELLO-WORLD-PYTHON'
    
    # Test with different delimiter
    space_result = string_join_split_patterns("a b c", " ")
    assert space_result['split_result'] == ['a', 'b', 'c']


# Test cases for Exercise 5
def test_nested_list_patterns():
    result = nested_list_patterns([[1, 2], [3, 4], [5]])
    assert result['flattened'] == [1, 2, 3, 4, 5]
    assert result['lengths'] == [2, 2, 1]
    assert result['max_in_each'] == [2, 4, 5]
    
    # Test with empty nested list
    empty_result = nested_list_patterns([[], [1], []])
    assert empty_result['flattened'] == [1]


if __name__ == "__main__":
    # Run all tests
    test_reverse_list_patterns()
    test_subarray_slicing_patterns()
    test_list_comprehension_filtering()
    test_string_join_split_patterns()
    test_nested_list_patterns()
    print("All tests passed!")