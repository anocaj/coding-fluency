"""
Tree Operations Drills

This file contains mini-exercises focused on binary tree traversal and manipulation.
Each function includes a stub with docstring and test cases to validate your implementation.

Topics covered:
- Tree traversal (inorder, preorder, postorder)
- Tree depth and height calculations
- Tree validation
- Path finding
- Tree construction
"""


class TreeNode:
    """Binary tree node definition."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __eq__(self, other):
        """Helper for testing tree equality."""
        if not other:
            return False
        return (self.val == other.val and 
                self.left == other.left and 
                self.right == other.right)


def inorder_traversal(root):
    """
    Perform inorder traversal of binary tree (left, root, right).
    
    Args:
        root (TreeNode): Root of binary tree
        
    Returns:
        List[int]: Values in inorder sequence
        
    Example:
        Tree:    1
                  \
                   2
                  /
                 3
        inorder_traversal(root) -> [1, 3, 2]
    """
    # TODO: Implement recursive inorder traversal
    pass


def max_depth(root):
    """
    Find maximum depth (height) of binary tree.
    
    Args:
        root (TreeNode): Root of binary tree
        
    Returns:
        int: Maximum depth of tree
        
    Example:
        Tree:    3
                / \
               9   20
                  /  \
                 15   7
        max_depth(root) -> 3
    """
    # TODO: Implement using recursion
    pass


def is_valid_bst(root):
    """
    Check if binary tree is a valid binary search tree.
    
    Args:
        root (TreeNode): Root of binary tree
        
    Returns:
        bool: True if valid BST, False otherwise
        
    Example:
        Tree:    2
                / \
               1   3
        is_valid_bst(root) -> True
        
    BST property: left subtree < root < right subtree for all nodes
    """
    # TODO: Implement with bounds checking
    pass


def has_path_sum(root, target_sum):
    """
    Check if tree has root-to-leaf path with given sum.
    
    Args:
        root (TreeNode): Root of binary tree
        target_sum (int): Target sum to find
        
    Returns:
        bool: True if path exists, False otherwise
        
    Example:
        Tree:      5
                  / \
                 4   8
                /   / \
               11  13  4
              /  \      \
             7    2      1
        has_path_sum(root, 22) -> True (5->4->11->2)
    """
    # TODO: Implement recursive path sum checking
    pass


def level_order_traversal(root):
    """
    Perform level-order (breadth-first) traversal of binary tree.
    
    Args:
        root (TreeNode): Root of binary tree
        
    Returns:
        List[List[int]]: Values grouped by level
        
    Example:
        Tree:    3
                / \
               9   20
                  /  \
                 15   7
        level_order_traversal(root) -> [[3], [9, 20], [15, 7]]
    """
    # TODO: Implement using queue (BFS)
    pass


# Helper function to create test trees
def create_test_tree():
    """Create a sample tree for testing."""
    #     3
    #    / \
    #   9   20
    #      /  \
    #     15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root


def create_bst():
    """Create a valid BST for testing."""
    #     2
    #    / \
    #   1   3
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    return root


def create_path_sum_tree():
    """Create tree for path sum testing."""
    #       5
    #      / \
    #     4   8
    #    /   / \
    #   11  13  4
    #  /  \      \
    # 7    2      1
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.right = TreeNode(1)
    return root


# Test cases for validation
def test_trees():
    """Test all tree drill functions."""
    
    # Test inorder_traversal
    print("Testing inorder_traversal...")
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    assert inorder_traversal(root) == [1, 3, 2]
    assert inorder_traversal(None) == []
    print("✓ inorder_traversal tests passed")
    
    # Test max_depth
    print("Testing max_depth...")
    tree = create_test_tree()
    assert max_depth(tree) == 3
    assert max_depth(None) == 0
    assert max_depth(TreeNode(1)) == 1
    print("✓ max_depth tests passed")
    
    # Test is_valid_bst
    print("Testing is_valid_bst...")
    bst = create_bst()
    assert is_valid_bst(bst) == True
    
    # Invalid BST
    invalid = TreeNode(5)
    invalid.left = TreeNode(1)
    invalid.right = TreeNode(4)
    invalid.right.left = TreeNode(3)
    invalid.right.right = TreeNode(6)
    assert is_valid_bst(invalid) == False
    
    assert is_valid_bst(None) == True
    print("✓ is_valid_bst tests passed")
    
    # Test has_path_sum
    print("Testing has_path_sum...")
    path_tree = create_path_sum_tree()
    assert has_path_sum(path_tree, 22) == True  # 5->4->11->2
    assert has_path_sum(path_tree, 26) == True  # 5->8->13
    assert has_path_sum(path_tree, 100) == False
    assert has_path_sum(None, 0) == False
    print("✓ has_path_sum tests passed")
    
    # Test level_order_traversal
    print("Testing level_order_traversal...")
    tree = create_test_tree()
    result = level_order_traversal(tree)
    expected = [[3], [9, 20], [15, 7]]
    assert result == expected
    assert level_order_traversal(None) == []
    print("✓ level_order_traversal tests passed")
    
    print("All tree drill tests completed!")


if __name__ == "__main__":
    test_trees()