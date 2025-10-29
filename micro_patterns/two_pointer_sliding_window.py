"""
Daily Warm-up: Two-Pointer and Sliding Window Patterns
======================================================
Time: 10-15 minutes daily practice
Focus: Algorithmic optimization patterns and efficient array processing

Instructions:
- Practice one exercise at a time
- Focus on speed and accuracy
- Repeat exercises until patterns become automatic
- Time yourself to build fluency

Usage: Run `python two_pointer_sliding_window.py` to execute all tests
"""

# Exercise 1: Converging Two-Pointers Pattern
def two_pointers_converging(arr, target_sum):
    """
    Demonstrate two pointers moving from ends toward center.
    
    Args:
        arr: Sorted array of numbers
        target_sum: Target sum to find
    
    Returns:
        tuple: Indices of two numbers that sum to target, or None if not found
        
    Example:
        >>> two_pointers_converging([1, 2, 3, 4, 5], 7)
        (1, 3)
    """
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return (left, right)
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1
    
    return None

# Exercise 2: Fixed Sliding Window Pattern
def fixed_sliding_window(arr, window_size):
    """
    Demonstrate sliding window with constant size for sum calculations.
    
    Args:
        arr: Array of numbers
        window_size: Size of the sliding window
    
    Returns:
        list: Sums of each window position
        
    Example:
        >>> fixed_sliding_window([1, 2, 3, 4, 5], 3)
        [6, 9, 12]
    """
    if len(arr) < window_size:
        return []
    
    window_sums = []
    
    # Calculate sum of first window
    window_sum = sum(arr[:window_size])
    window_sums.append(window_sum)
    
    # Slide the window: remove leftmost element, add new rightmost element
    for i in range(window_size, len(arr)):
        window_sum = window_sum - arr[i - window_size] + arr[i]
        window_sums.append(window_sum)
    
    return window_sums

# Exercise 3: Variable Sliding Window Pattern
def variable_sliding_window(arr, target_sum):
    """
    Demonstrate expanding/contracting window based on conditions.
    
    Args:
        arr: Array of positive numbers
        target_sum: Target sum to achieve
    
    Returns:
        tuple: (start_index, end_index) of subarray with target sum, or None
        
    Example:
        >>> variable_sliding_window([1, 2, 3, 4, 5], 9)
        (1, 3)
    """
    left = 0
    current_sum = 0
    
    for right in range(len(arr)):
        # Expand window by adding current element
        current_sum += arr[right]
        
        # Contract window from left while sum is too large
        while current_sum > target_sum and left <= right:
            current_sum -= arr[left]
            left += 1
        
        # Check if we found the target sum
        if current_sum == target_sum:
            return (left, right)
    
    return None

# Exercise 4: Cumulative Sum Tracking Pattern
def cumulative_sum_window(arr, window_size):
    """
    Demonstrate cumulative sum tracking in sliding windows.
    
    Args:
        arr: Array of numbers
        window_size: Size of the sliding window
    
    Returns:
        tuple: (window_sums, max_sum, max_sum_index)
        
    Example:
        >>> cumulative_sum_window([1, 3, 2, 6, 1], 3)
        ([6, 11, 9], 11, 1)
    """
    if len(arr) < window_size:
        return ([], None, None)
    
    window_sums = []
    
    # Calculate sum of first window
    window_sum = sum(arr[:window_size])
    window_sums.append(window_sum)
    max_sum = window_sum
    max_sum_index = 0
    
    # Slide the window and track maximum
    for i in range(window_size, len(arr)):
        window_sum = window_sum - arr[i - window_size] + arr[i]
        window_sums.append(window_sum)
        
        # Update maximum sum and its index
        if window_sum > max_sum:
            max_sum = window_sum
            max_sum_index = i - window_size + 1
    
    return (window_sums, max_sum, max_sum_index)

# Test cases
def test_two_pointers_converging():
    assert two_pointers_converging([1, 2, 3, 4, 5], 7) == (1, 3)
    assert two_pointers_converging([1, 2, 3, 4], 10) is None
    assert two_pointers_converging([1, 2], 3) == (0, 1)

def test_fixed_sliding_window():
    assert fixed_sliding_window([1, 2, 3, 4, 5], 3) == [6, 9, 12]
    assert fixed_sliding_window([1, 1, 1], 2) == [2, 2]
    assert fixed_sliding_window([5], 1) == [5]

def test_variable_sliding_window():
    assert variable_sliding_window([1, 2, 3, 4, 5], 9) == (1, 3)
    assert variable_sliding_window([1, 2, 3], 10) is None
    assert variable_sliding_window([5], 5) == (0, 0)

def test_cumulative_sum_window():
    window_sums, max_sum, max_index = cumulative_sum_window([1, 3, 2, 6, 1], 3)
    assert window_sums == [6, 11, 9]
    assert max_sum == 11
    assert max_index == 1

if __name__ == "__main__":
    test_two_pointers_converging()
    test_fixed_sliding_window()
    test_variable_sliding_window()
    test_cumulative_sum_window()
    print("All two-pointer and sliding window pattern tests passed!")