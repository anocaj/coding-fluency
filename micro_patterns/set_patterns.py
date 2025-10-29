"""
Daily Warm-up: Set Patterns
============================
Time: 10-15 minutes daily practice
Focus: Set operations, uniqueness, and efficient membership testing

Instructions:
- Practice one exercise at a time
- Focus on speed and accuracy with set operations
- Repeat exercises until set patterns become automatic
- Time yourself to build fluency with set-based solutions

Usage: Run `python set_patterns.py` to execute all tests
"""


# Exercise 1: Unique Elements
def find_unique_elements(arr):
    """
    Remove duplicates from a list using set operations.
    
    Args:
        arr: List that may contain duplicate elements
    
    Returns:
        list: List of unique elements (order may not be preserved)
        
    Example:
        >>> find_unique_elements([1, 2, 2, 3, 1, 4])
        [1, 2, 3, 4]  # Order may vary
    """
    # Convert to set to remove duplicates, then back to list
    return list(set(arr))


# Exercise 2: Membership Testing
def efficient_membership_check(items, search_list):
    """
    Check if items exist in a collection using efficient set-based lookup.
    
    Args:
        items: List of items to search for
        search_list: List to search within
    
    Returns:
        list: Boolean list indicating which items were found
        
    Example:
        >>> efficient_membership_check([1, 5, 9], [1, 2, 3, 4, 5])
        [True, True, False]
    """
    # Convert search_list to set for O(1) lookup time
    search_set = set(search_list)
    
    # Check membership for each item using set lookup
    return [item in search_set for item in items]


# Exercise 3: Set Operations
def set_operations_demo(set1, set2):
    """
    Demonstrate intersection, union, and difference operations on sets.
    
    Args:
        set1: First set of elements
        set2: Second set of elements
    
    Returns:
        dict: Dictionary with 'intersection', 'union', and 'difference' keys
        
    Example:
        >>> set_operations_demo([1, 2, 3], [2, 3, 4])
        {'intersection': {2, 3}, 'union': {1, 2, 3, 4}, 'difference': {1}}
    """
    # Convert inputs to sets
    s1 = set(set1)
    s2 = set(set2)
    
    return {
        'intersection': s1 & s2,  # Elements in both sets
        'union': s1 | s2,        # Elements in either set
        'difference': s1 - s2    # Elements in s1 but not in s2
    }


# Exercise 4: Set Comprehensions and Advanced Operations
def advanced_set_operations(data):
    """
    Use set comprehensions and advanced set operations for data processing.
    
    Args:
        data: List of numbers
    
    Returns:
        dict: Dictionary with various set-based analyses
        
    Example:
        >>> advanced_set_operations([1, 2, 3, 4, 5, 6])
        {'evens': {2, 4, 6}, 'odds': {1, 3, 5}, 'squares': {1, 4, 9, 16, 25, 36}}
    """
    # Use set comprehensions for efficient filtering and transformation
    return {
        'evens': {x for x in data if x % 2 == 0},
        'odds': {x for x in data if x % 2 == 1},
        'squares': {x * x for x in data}
    }


# Test cases for Exercise 1
def test_find_unique_elements():
    result = find_unique_elements([1, 2, 2, 3, 1, 4])
    assert set(result) == {1, 2, 3, 4}
    
    result = find_unique_elements([])
    assert result == []
    
    result = find_unique_elements([5, 5, 5])
    assert result == [5]
    
    result = find_unique_elements([1, 2, 3])
    assert set(result) == {1, 2, 3}


# Test cases for Exercise 2
def test_efficient_membership_check():
    result = efficient_membership_check([1, 5, 9], [1, 2, 3, 4, 5])
    assert result == [True, True, False]
    
    result = efficient_membership_check([], [1, 2, 3])
    assert result == []
    
    result = efficient_membership_check([10, 20], [])
    assert result == [False, False]
    
    result = efficient_membership_check([1, 1, 2], [1, 2, 3])
    assert result == [True, True, True]


# Test cases for Exercise 3
def test_set_operations_demo():
    result = set_operations_demo([1, 2, 3], [2, 3, 4])
    assert result['intersection'] == {2, 3}
    assert result['union'] == {1, 2, 3, 4}
    assert result['difference'] == {1}
    
    result = set_operations_demo([1, 2], [3, 4])
    assert result['intersection'] == set()
    assert result['union'] == {1, 2, 3, 4}
    assert result['difference'] == {1, 2}
    
    result = set_operations_demo([1, 2, 3], [1, 2, 3])
    assert result['intersection'] == {1, 2, 3}
    assert result['union'] == {1, 2, 3}
    assert result['difference'] == set()


# Test cases for Exercise 4
def test_advanced_set_operations():
    result = advanced_set_operations([1, 2, 3, 4, 5, 6])
    assert result['evens'] == {2, 4, 6}
    assert result['odds'] == {1, 3, 5}
    assert result['squares'] == {1, 4, 9, 16, 25, 36}
    
    result = advanced_set_operations([])
    assert result['evens'] == set()
    assert result['odds'] == set()
    assert result['squares'] == set()
    
    result = advanced_set_operations([2, 4])
    assert result['evens'] == {2, 4}
    assert result['odds'] == set()
    assert result['squares'] == {4, 16}


if __name__ == "__main__":
    test_find_unique_elements()
    test_efficient_membership_check()
    test_set_operations_demo()
    test_advanced_set_operations()
    print("All tests passed!")