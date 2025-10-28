"""
Dynamic Programming Drills

This file contains mini-exercises focused on dynamic programming patterns and techniques.
Each function includes a stub with docstring and test cases to validate your implementation.

Topics covered:
- Memoization (top-down DP)
- Tabulation (bottom-up DP)
- Classic DP problems
- Optimization problems
- Sequence and subsequence problems
"""


def fibonacci_dp(n):
    """
    Calculate nth Fibonacci number using dynamic programming (memoization).
    
    Args:
        n (int): Position in Fibonacci sequence
        
    Returns:
        int: nth Fibonacci number
        
    Example:
        fibonacci_dp(10) -> 55
        fibonacci_dp(0) -> 0
        fibonacci_dp(1) -> 1
        
    Note: This should be much faster than naive recursion for large n.
    """
    # TODO: Implement using memoization or tabulation
    pass


def climbing_stairs(n):
    """
    Count number of ways to climb n stairs (can take 1 or 2 steps at a time).
    
    Args:
        n (int): Number of stairs
        
    Returns:
        int: Number of distinct ways to climb stairs
        
    Example:
        climbing_stairs(2) -> 2  # (1+1) or (2)
        climbing_stairs(3) -> 3  # (1+1+1), (1+2), or (2+1)
        
    Recurrence: ways(n) = ways(n-1) + ways(n-2)
    """
    # TODO: Implement using DP (similar to Fibonacci)
    pass


def coin_change(coins, amount):
    """
    Find minimum number of coins needed to make the given amount.
    
    Args:
        coins (List[int]): Available coin denominations
        amount (int): Target amount
        
    Returns:
        int: Minimum number of coins needed, -1 if impossible
        
    Example:
        coin_change([1, 3, 4], 6) -> 2  # (3 + 3)
        coin_change([2], 3) -> -1       # impossible
        
    DP state: dp[i] = minimum coins needed for amount i
    """
    # TODO: Implement using bottom-up DP
    pass


def longest_increasing_subsequence(nums):
    """
    Find length of longest increasing subsequence.
    
    Args:
        nums (List[int]): Array of integers
        
    Returns:
        int: Length of longest increasing subsequence
        
    Example:
        longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) -> 4
        # LIS: [2, 3, 7, 18] or [2, 3, 7, 101]
        
    DP state: dp[i] = length of LIS ending at index i
    """
    # TODO: Implement using DP with O(n²) solution
    pass


def knapsack_01(weights, values, capacity):
    """
    Solve 0/1 knapsack problem using dynamic programming.
    
    Args:
        weights (List[int]): Weight of each item
        values (List[int]): Value of each item
        capacity (int): Maximum weight capacity
        
    Returns:
        int: Maximum value that can be obtained
        
    Example:
        weights = [1, 3, 4, 5]
        values = [1, 4, 5, 7]
        capacity = 7
        knapsack_01(weights, values, 7) -> 9  # items with weights [3, 4]
        
    DP state: dp[i][w] = max value using first i items with weight limit w
    """
    # TODO: Implement using 2D DP table
    pass


# Test cases for validation
def test_dynamic_programming():
    """Test all dynamic programming drill functions."""
    
    # Test fibonacci_dp
    print("Testing fibonacci_dp...")
    assert fibonacci_dp(0) == 0
    assert fibonacci_dp(1) == 1
    assert fibonacci_dp(10) == 55
    assert fibonacci_dp(15) == 610
    # Test that it's efficient enough for larger numbers
    assert fibonacci_dp(30) == 832040
    print("✓ fibonacci_dp tests passed")
    
    # Test climbing_stairs
    print("Testing climbing_stairs...")
    assert climbing_stairs(1) == 1
    assert climbing_stairs(2) == 2
    assert climbing_stairs(3) == 3
    assert climbing_stairs(4) == 5
    assert climbing_stairs(5) == 8
    print("✓ climbing_stairs tests passed")
    
    # Test coin_change
    print("Testing coin_change...")
    assert coin_change([1, 3, 4], 6) == 2
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
    assert coin_change([1, 2, 5], 11) == 3  # 5 + 5 + 1
    assert coin_change([2, 5, 10, 1], 27) == 4  # 10 + 10 + 5 + 2
    print("✓ coin_change tests passed")
    
    # Test longest_increasing_subsequence
    print("Testing longest_increasing_subsequence...")
    assert longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert longest_increasing_subsequence([0, 1, 0, 3, 2, 3]) == 4
    assert longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7]) == 1
    assert longest_increasing_subsequence([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6
    print("✓ longest_increasing_subsequence tests passed")
    
    # Test knapsack_01
    print("Testing knapsack_01...")
    weights1 = [1, 3, 4, 5]
    values1 = [1, 4, 5, 7]
    assert knapsack_01(weights1, values1, 7) == 9
    
    weights2 = [2, 1, 3, 2]
    values2 = [12, 10, 20, 15]
    assert knapsack_01(weights2, values2, 5) == 37  # items 0, 1, 3
    
    # Edge cases
    assert knapsack_01([], [], 10) == 0
    assert knapsack_01([1, 2], [1, 2], 0) == 0
    print("✓ knapsack_01 tests passed")
    
    print("All dynamic programming drill tests completed!")


if __name__ == "__main__":
    test_dynamic_programming()