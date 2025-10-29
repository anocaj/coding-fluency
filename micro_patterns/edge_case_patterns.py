"""
Daily Warm-up: Edge Case Patterns
=================================
Time: 10-15 minutes daily practice
Focus: Boundary conditions and defensive programming

Instructions:
- Practice one exercise at a time
- Focus on speed and accuracy
- Repeat exercises until patterns become automatic
- Time yourself to build fluency

Usage: Run `python edge_case_patterns.py` to execute all tests
"""

# Exercise 1: Empty Input Validation Pattern
def handle_empty_input(arr, default_value=None):
    """
    Demonstrate empty input checks and guard clauses.
    
    Args:
        arr: List that might be empty or None
        default_value: Value to return for empty/None input
    
    Returns:
        any: First element of array or default value
        
    Example:
        >>> handle_empty_input([1, 2, 3])
        1
        >>> handle_empty_input([], "empty")
        'empty'
        >>> handle_empty_input(None, "none")
        'none'
    """
    pass

# Exercise 2: Single-Element Edge Case Pattern
def handle_single_element(arr):
    """
    Demonstrate special handling for single-element collections.
    
    Args:
        arr: List that might have only one element
    
    Returns:
        tuple: (is_single_element, processed_result)
        
    Example:
        >>> handle_single_element([42])
        (True, 42)
        >>> handle_single_element([1, 2, 3])
        (False, [1, 2, 3])
    """
    pass

# Exercise 3: Boundary Checks Pattern
def safe_array_access(arr, index, default=None):
    """
    Demonstrate index validation and bounds checking.
    
    Args:
        arr: List to access
        index: Index to access (may be out of bounds)
        default: Value to return if index is invalid
    
    Returns:
        any: Element at index or default value
        
    Example:
        >>> safe_array_access([1, 2, 3], 1)
        2
        >>> safe_array_access([1, 2, 3], 5, "out of bounds")
        'out of bounds'
    """
    pass

# Exercise 4: Type and None Validation Pattern
def validate_input_types(value, expected_type, allow_none=False):
    """
    Demonstrate input validation and type checking.
    
    Args:
        value: Value to validate
        expected_type: Expected type for the value
        allow_none: Whether None is acceptable
    
    Returns:
        tuple: (is_valid, processed_value)
        
    Example:
        >>> validate_input_types(42, int)
        (True, 42)
        >>> validate_input_types("hello", int)
        (False, None)
        >>> validate_input_types(None, str, allow_none=True)
        (True, None)
    """
    pass

# Test cases
def test_handle_empty_input():
    assert handle_empty_input([1, 2, 3]) == 1
    assert handle_empty_input([], "empty") == "empty"
    assert handle_empty_input(None, "none") == "none"
    assert handle_empty_input([42]) == 42

def test_handle_single_element():
    assert handle_single_element([42]) == (True, 42)
    assert handle_single_element([1, 2, 3]) == (False, [1, 2, 3])
    assert handle_single_element([]) == (False, [])

def test_safe_array_access():
    assert safe_array_access([1, 2, 3], 1) == 2
    assert safe_array_access([1, 2, 3], 5, "out of bounds") == "out of bounds"
    assert safe_array_access([], 0, "empty") == "empty"
    assert safe_array_access([1, 2, 3], -1) == 3

def test_validate_input_types():
    assert validate_input_types(42, int) == (True, 42)
    assert validate_input_types("hello", int) == (False, None)
    assert validate_input_types(None, str, allow_none=True) == (True, None)
    assert validate_input_types(None, str, allow_none=False) == (False, None)

if __name__ == "__main__":
    test_handle_empty_input()
    test_handle_single_element()
    test_safe_array_access()
    test_validate_input_types()
    print("All edge case pattern tests passed!")