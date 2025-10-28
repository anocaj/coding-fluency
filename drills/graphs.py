"""
Graph Algorithms Drills

This file contains mini-exercises focused on graph traversal and algorithms.
Each function includes a stub with docstring and test cases to validate your implementation.

Topics covered:
- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Path finding
- Connected components
- Cycle detection
"""

from collections import deque, defaultdict


def dfs_recursive(graph, start, visited=None):
    """
    Perform Depth-First Search using recursion.
    
    Args:
        graph (dict): Adjacency list representation {node: [neighbors]}
        start: Starting node
        visited (set): Set of visited nodes (for recursion)
        
    Returns:
        List: Nodes in DFS order
        
    Example:
        graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
        dfs_recursive(graph, 2) -> [2, 0, 1, 3]
    """
    # TODO: Implement recursive DFS
    pass


def bfs(graph, start):
    """
    Perform Breadth-First Search using a queue.
    
    Args:
        graph (dict): Adjacency list representation {node: [neighbors]}
        start: Starting node
        
    Returns:
        List: Nodes in BFS order
        
    Example:
        graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
        bfs(graph, 2) -> [2, 0, 3, 1]
    """
    # TODO: Implement BFS using queue
    pass


def has_path(graph, start, end):
    """
    Check if there's a path between start and end nodes using DFS.
    
    Args:
        graph (dict): Adjacency list representation
        start: Starting node
        end: Target node
        
    Returns:
        bool: True if path exists, False otherwise
        
    Example:
        graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: []}
        has_path(graph, 0, 3) -> True
        has_path(graph, 3, 0) -> False
    """
    # TODO: Implement path finding using DFS
    pass


def connected_components(graph):
    """
    Find all connected components in an undirected graph.
    
    Args:
        graph (dict): Adjacency list representation
        
    Returns:
        List[List]: List of connected components
        
    Example:
        graph = {0: [1], 1: [0], 2: [3], 3: [2], 4: []}
        connected_components(graph) -> [[0, 1], [2, 3], [4]]
    """
    # TODO: Implement using DFS to find components
    pass


def has_cycle(graph):
    """
    Detect if undirected graph has a cycle using DFS.
    
    Args:
        graph (dict): Adjacency list representation of undirected graph
        
    Returns:
        bool: True if cycle exists, False otherwise
        
    Example:
        graph = {0: [1, 2], 1: [0, 2], 2: [0, 1]}  # Triangle
        has_cycle(graph) -> True
        
        graph = {0: [1], 1: [0, 2], 2: [1]}  # Tree
        has_cycle(graph) -> False
    """
    # TODO: Implement cycle detection using DFS
    pass


# Helper functions for testing
def create_sample_graph():
    """Create a sample directed graph for testing."""
    return {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [3]
    }


def create_undirected_graph():
    """Create a sample undirected graph for testing."""
    return {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }


def create_disconnected_graph():
    """Create a graph with multiple components."""
    return {
        0: [1],
        1: [0],
        2: [3],
        3: [2],
        4: []
    }


def create_cyclic_graph():
    """Create an undirected graph with a cycle."""
    return {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1]
    }


def create_acyclic_graph():
    """Create an undirected graph without cycles (tree)."""
    return {
        0: [1],
        1: [0, 2],
        2: [1]
    }


# Test cases for validation
def test_graphs():
    """Test all graph drill functions."""
    
    # Test dfs_recursive
    print("Testing dfs_recursive...")
    graph = create_sample_graph()
    result = dfs_recursive(graph, 2)
    # DFS can have multiple valid orders, check if it visits all reachable nodes
    assert len(result) == 4
    assert set(result) == {0, 1, 2, 3}
    assert result[0] == 2  # Should start with the start node
    print("✓ dfs_recursive tests passed")
    
    # Test bfs
    print("Testing bfs...")
    result = bfs(graph, 2)
    assert len(result) == 4
    assert set(result) == {0, 1, 2, 3}
    assert result[0] == 2  # Should start with the start node
    print("✓ bfs tests passed")
    
    # Test has_path
    print("Testing has_path...")
    assert has_path(graph, 0, 3) == True
    assert has_path(graph, 2, 1) == True
    
    # Test with disconnected nodes
    disconnected = {0: [1], 1: [0], 2: []}
    assert has_path(disconnected, 0, 2) == False
    assert has_path(disconnected, 0, 1) == True
    print("✓ has_path tests passed")
    
    # Test connected_components
    print("Testing connected_components...")
    disc_graph = create_disconnected_graph()
    components = connected_components(disc_graph)
    
    # Sort components for consistent testing
    components = [sorted(comp) for comp in components]
    components.sort()
    
    expected = [[0, 1], [2, 3], [4]]
    assert components == expected
    print("✓ connected_components tests passed")
    
    # Test has_cycle
    print("Testing has_cycle...")
    cyclic = create_cyclic_graph()
    acyclic = create_acyclic_graph()
    
    assert has_cycle(cyclic) == True
    assert has_cycle(acyclic) == False
    
    # Single node
    single_node = {0: []}
    assert has_cycle(single_node) == False
    print("✓ has_cycle tests passed")
    
    print("All graph drill tests completed!")


if __name__ == "__main__":
    test_graphs()