"""
Array Manipulation Drills

This file contains mini-exercises focused on common array patterns and operations.
Each function includes a stub with docstring and test cases to validate your implementation.

Topics covered:
- Two-pointer technique
- Sliding window
- Array rotation
- Subarray problems
- In-place modifications
"""


def two_sum(nums, target):
    """
    Find two numbers in the array that add up to the target.
    
    Args:
        nums (List[int]): Array of integers
        target (int): Target sum
        
    Returns:
        List[int]: Indices of the two numbers that add up to target
        
    Example:
        two_sum([2, 7, 11, 15], 9) -> [0, 1]
    """
    # TODO: Implement using hash map for O(n) solution
    pass


def max_subarray_sum(nums):
    """
    Find the maximum sum of a contiguous subarray (Kadane's algorithm).
    
    Args:
        nums (List[int]): Array of integers
        
    Returns:
        int: Maximum sum of contiguous subarray
        
    Example:
        max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) -> 6
    """
    # TODO: Implement Kadane's algorithm
    pass


def rotate_array(nums, k):
    """
    Rotate array to the right by k steps in-place.
    
    Args:
        nums (List[int]): Array to rotate (modified in-place)
        k (int): Number of steps to rotate right
        
    Returns:
        None: Modifies array in-place
        
    Example:
        nums = [1, 2, 3, 4, 5, 6, 7], k = 3
        After rotation: [5, 6, 7, 1, 2, 3, 4]
    """
    # TODO: Implement using array reversal technique
    pass


def remove_duplicates(nums):
    """
    Remove duplicates from sorted array in-place and return new length.
    
    Args:
        nums (List[int]): Sorted array with duplicates
        
    Returns:
        int: Length of array after removing duplicates
        
    Example:
        remove_duplicates([1, 1, 2, 2, 3]) -> 3
        nums becomes [1, 2, 3, _, _]
    """
    # TODO: Implement using two-pointer technique
    pass


def merge_sorted_arrays(nums1, m, nums2, n):
    """
    Merge two sorted arrays in-place into nums1.
    
    Args:
        nums1 (List[int]): First sorted array with extra space at end
        m (int): Number of elements in nums1
        nums2 (List[int]): Second sorted array
        n (int): Number of elements in nums2
        
    Returns:
        None: Modifies nums1 in-place
        
    Example:
        nums1 = [1, 2, 3, 0, 0, 0], m = 3
        nums2 = [2, 5, 6], n = 3
        Result: nums1 = [1, 2, 2, 3, 5, 6]
    """
    # TODO: Implement merging from the end to avoid overwriting
    pass


# Test cases for validation
def test_arrays():
    """Test all array drill functions."""
    
    # Test two_sum
    print("Testing two_sum...")
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    print("✓ two_sum tests passed")
    
    # Test max_subarray_sum
    print("Testing max_subarray_sum...")
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray_sum([1]) == 1
    assert max_subarray_sum([5, 4, -1, 7, 8]) == 23
    print("✓ max_subarray_sum tests passed")
    
    # Test rotate_array
    print("Testing rotate_array...")
    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate_array(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]
    
    nums = [-1, -100, 3, 99]
    rotate_array(nums, 2)
    assert nums == [3, 99, -1, -100]
    print("✓ rotate_array tests passed")
    
    # Test remove_duplicates
    print("Testing remove_duplicates...")
    nums = [1, 1, 2]
    assert remove_duplicates(nums) == 2
    assert nums[:2] == [1, 2]
    
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert remove_duplicates(nums) == 5
    assert nums[:5] == [0, 1, 2, 3, 4]
    print("✓ remove_duplicates tests passed")
    
    # Test merge_sorted_arrays
    print("Testing merge_sorted_arrays...")
    nums1 = [1, 2, 3, 0, 0, 0]
    merge_sorted_arrays(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]
    
    nums1 = [1]
    merge_sorted_arrays(nums1, 1, [], 0)
    assert nums1 == [1]
    print("✓ merge_sorted_arrays tests passed")
    
    print("All array drill tests completed!")


if __name__ == "__main__":
    test_arrays()