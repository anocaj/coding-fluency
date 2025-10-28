"""
Recursion Drills

This file contains mini-exercises focused on recursive problem solving.
Each function includes a stub with docstring and test cases to validate your implementation.

Topics covered:
- Base case and recursive case identification
- Tree-like recursion
- Backtracking
- Divide and conquer
- Memoization basics
"""


def factorial(n):
    """
    Calculate factorial of n using recursion.
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Factorial of n
        
    Example:
        factorial(5) -> 120
        factorial(0) -> 1
        
    Base case: factorial(0) = 1
    Recursive case: factorial(n) = n * factorial(n-1)
    """
    # TODO: Implement with proper base case and recursive case
    pass


def fibonacci(n):
    """
    Calculate nth Fibonacci number using recursion.
    
    Args:
        n (int): Position in Fibonacci sequence (0-indexed)
        
    Returns:
        int: nth Fibonacci number
        
    Example:
        fibonacci(6) -> 8
        fibonacci(0) -> 0
        fibonacci(1) -> 1
        
    Base cases: fib(0) = 0, fib(1) = 1
    Recursive case: fib(n) = fib(n-1) + fib(n-2)
    """
    # TODO: Implement basic recursion (note: this will be slow for large n)
    pass


def power(base, exponent):
    """
    Calculate base^exponent using recursion (divide and conquer approach).
    
    Args:
        base (int): Base number
        exponent (int): Non-negative exponent
        
    Returns:
        int: Result of base^exponent
        
    Example:
        power(2, 8) -> 256
        power(3, 4) -> 81
        
    Base case: power(base, 0) = 1
    Recursive case: 
        - If exponent is even: power(base, exp) = power(base, exp/2)^2
        - If exponent is odd: power(base, exp) = base * power(base, exp-1)
    """
    # TODO: Implement efficient recursive power calculation
    pass


def reverse_string(s):
    """
    Reverse a string using recursion.
    
    Args:
        s (str): Input string to reverse
        
    Returns:
        str: Reversed string
        
    Example:
        reverse_string("hello") -> "olleh"
        reverse_string("a") -> "a"
        
    Base case: empty string or single character
    Recursive case: last_char + reverse(rest_of_string)
    """
    # TODO: Implement string reversal recursively
    pass


def generate_parentheses(n):
    """
    Generate all valid combinations of n pairs of parentheses using backtracking.
    
    Args:
        n (int): Number of pairs of parentheses
        
    Returns:
        List[str]: All valid parentheses combinations
        
    Example:
        generate_parentheses(3) -> ["((()))", "(()())", "(())()", "()(())", "()()()"]
        generate_parentheses(1) -> ["()"]
        
    Backtracking approach:
    - Add '(' if we haven't used all opening brackets
    - Add ')' if it won't exceed opening brackets
    - Base case: when we've used all n pairs
    """
    # TODO: Implement using backtracking recursion
    pass


# Test cases for validation
def test_recursion():
    """Test all recursion drill functions."""
    
    # Test factorial
    print("Testing factorial...")
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(7) == 5040
    print("✓ factorial tests passed")
    
    # Test fibonacci
    print("Testing fibonacci...")
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(6) == 8
    assert fibonacci(10) == 55
    print("✓ fibonacci tests passed")
    
    # Test power
    print("Testing power...")
    assert power(2, 0) == 1
    assert power(2, 8) == 256
    assert power(3, 4) == 81
    assert power(5, 3) == 125
    print("✓ power tests passed")
    
    # Test reverse_string
    print("Testing reverse_string...")
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("hello") == "olleh"
    assert reverse_string("recursion") == "noisrucer"
    print("✓ reverse_string tests passed")
    
    # Test generate_parentheses
    print("Testing generate_parentheses...")
    result1 = generate_parentheses(1)
    assert sorted(result1) == ["()"]
    
    result2 = generate_parentheses(2)
    assert sorted(result2) == ["(())", "()()"]
    
    result3 = generate_parentheses(3)
    expected3 = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert sorted(result3) == sorted(expected3)
    print("✓ generate_parentheses tests passed")
    
    print("All recursion drill tests completed!")


if __name__ == "__main__":
    test_recursion()