"""
Daily Warm-up: Frequency Counting Patterns
==========================================
Time: 10-15 minutes daily practice
Focus: Frequency analysis and counting patterns for data analysis

Instructions:
- Practice one exercise at a time
- Focus on speed and accuracy with counting operations
- Repeat exercises until counting patterns become automatic
- Time yourself to build fluency with frequency analysis
- Master both Counter module and manual dictionary approaches

Usage: Run `python frequency_counting.py` to execute all tests
"""

from collections import Counter


# Exercise 1: Counter Module Usage
def counter_frequency_analysis(items):
    """
    Use collections.Counter for frequency analysis and common element operations.
    
    Args:
        items: List of elements to analyze
    
    Returns:
        tuple: (frequency_dict, most_common_element, most_common_count)
        
    Example:
        >>> counter_frequency_analysis(['a', 'b', 'a', 'c', 'b', 'a'])
        ({'a': 3, 'b': 2, 'c': 1}, 'a', 3)
    """
    # Create Counter object for frequency analysis
    counter = Counter(items)
    
    # Convert to regular dictionary
    frequency_dict = dict(counter)
    
    # Get most common element and its count
    if counter:
        most_common_element, most_common_count = counter.most_common(1)[0]
    else:
        most_common_element, most_common_count = None, 0
    
    return frequency_dict, most_common_element, most_common_count


# Exercise 2: Manual Dictionary Counting
def manual_frequency_counting(items):
    """
    Build frequency maps using manual dictionary operations without Counter.
    
    Args:
        items: List of elements to count
    
    Returns:
        dict: Frequency mapping of elements to their counts
        
    Example:
        >>> manual_frequency_counting([1, 2, 1, 3, 2, 1])
        {1: 3, 2: 2, 3: 1}
    """
    frequency_map = {}
    
    # Manual counting using dict.get() with default value
    for item in items:
        frequency_map[item] = frequency_map.get(item, 0) + 1
    
    return frequency_map


# Exercise 3: Conditional Counting with Generator Expressions
def conditional_counting(items, condition_func):
    """
    Count elements meeting specific conditions using sum() with generator expressions.
    
    Args:
        items: List of elements to evaluate
        condition_func: Function that returns True for elements to count
    
    Returns:
        int: Count of elements meeting the condition
        
    Example:
        >>> conditional_counting([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
        2
    """
    # Use sum() with generator expression for conditional counting
    return sum(1 for item in items if condition_func(item))


# Exercise 4: Frequency Analysis with Filtering
def frequency_with_filtering(text, min_frequency=2):
    """
    Analyze character frequency and filter results based on minimum occurrence.
    
    Args:
        text: String to analyze
        min_frequency: Minimum count to include in results
    
    Returns:
        dict: Characters that appear at least min_frequency times
        
    Example:
        >>> frequency_with_filtering("hello world", 2)
        {'l': 3}
    """
    # Count character frequencies manually
    char_counts = {}
    for char in text:
        if char != ' ':  # Skip spaces for cleaner analysis
            char_counts[char] = char_counts.get(char, 0) + 1
    
    # Filter results based on minimum frequency
    filtered_results = {char: count for char, count in char_counts.items() 
                       if count >= min_frequency}
    
    return filtered_results


# Test cases for Exercise 1
def test_counter_frequency_analysis():
    freq_dict, most_common, count = counter_frequency_analysis(['a', 'b', 'a', 'c', 'b', 'a'])
    assert freq_dict == {'a': 3, 'b': 2, 'c': 1}
    assert most_common == 'a'
    assert count == 3
    
    # Test with numbers
    freq_dict, most_common, count = counter_frequency_analysis([1, 2, 1, 1, 3])
    assert freq_dict == {1: 3, 2: 1, 3: 1}
    assert most_common == 1
    assert count == 3


# Test cases for Exercise 2
def test_manual_frequency_counting():
    assert manual_frequency_counting([1, 2, 1, 3, 2, 1]) == {1: 3, 2: 2, 3: 1}
    assert manual_frequency_counting(['x', 'y', 'x']) == {'x': 2, 'y': 1}
    assert manual_frequency_counting([]) == {}


# Test cases for Exercise 3
def test_conditional_counting():
    # Count even numbers
    assert conditional_counting([1, 2, 3, 4, 5], lambda x: x % 2 == 0) == 2
    # Count strings longer than 3 characters
    assert conditional_counting(['hi', 'hello', 'world', 'a'], lambda x: len(x) > 3) == 2
    # Count positive numbers
    assert conditional_counting([-1, 0, 1, 2, -3], lambda x: x > 0) == 2


# Test cases for Exercise 4
def test_frequency_with_filtering():
    assert frequency_with_filtering("hello world", 2) == {'l': 3, 'o': 2}
    assert frequency_with_filtering("programming", 2) == {'r': 2, 'g': 2, 'm': 2}
    assert frequency_with_filtering("abc", 2) == {}


if __name__ == "__main__":
    test_counter_frequency_analysis()
    test_manual_frequency_counting()
    test_conditional_counting()
    test_frequency_with_filtering()
    print("All frequency counting pattern tests passed!")