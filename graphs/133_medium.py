from typing import Optional

class Node:
    def __init__(self, val: int = 0, neighbors: list = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Clones a connected undirected graph.
        
        Problem Understanding:
        - Given a reference to a node in a connected undirected graph
        - Return a deep copy (clone) of the graph
        - Each node has a value and a list of neighbors
        
        Approach:
        - Use DFS/BFS with a hash map to keep track of already cloned nodes
        - The hash map prevents infinite loops and ensures each node is cloned only once
        - For each node, create a clone and recursively clone its neighbors
        - Store the mapping from original to cloned nodes in the hash map
        
        Time Complexity: O(N + M) where N is number of nodes and M is number of edges
        Space Complexity: O(N) for the hash map and recursion stack
        
        Args:
            node: Reference to the starting node of the graph
            
        Returns:
            Reference to the cloned graph starting from the equivalent of the input node
        """
        if not node:
            return None
        
        # Hash map to store mapping from original node to cloned node
        # This prevents infinite loops and ensures each node is cloned only once
        cloned = {}
        
        def dfs(original_node):
            # If we've already cloned this node, return the clone
            if original_node in cloned:
                return cloned[original_node]
            
            # Create a new node with the same value
            clone = Node(original_node.val)
            
            # Store the mapping before processing neighbors to handle cycles
            cloned[original_node] = clone
            
            # Clone all neighbors
            for neighbor in original_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)

def run_clone_graph_test(adj_list, expected_adj_list, test_name):
    """
    Tests the cloneGraph function.
    
    Args:
        adj_list: Adjacency list representation of the input graph
        expected_adj_list: Expected adjacency list of the cloned graph
        test_name: Name/description of the test case
    """
    # Helper function to create graph from adjacency list
    def create_graph_from_adj_list(adj_list):
        if not adj_list:
            return None
        
        # Create all nodes
        nodes = {}
        for i in range(1, len(adj_list) + 1):
            nodes[i] = Node(i)
        
        # Connect nodes according to adjacency list
        for i in range(len(adj_list)):
            node_val = i + 1
            for neighbor_val in adj_list[i]:
                nodes[node_val].neighbors.append(nodes[neighbor_val])
        
        return nodes[1]  # Return the first node
    
    # Helper function to convert graph back to adjacency list for comparison
    def graph_to_adj_list(node):
        if not node:
            return []
        
        visited = set()
        result = []
        
        def dfs(current_node):
            if current_node.val in visited:
                return
            visited.add(current_node.val)
            
            # Ensure result has enough space
            while len(result) < current_node.val:
                result.append([])
            
            # Add neighbors
            result[current_node.val - 1] = [neighbor.val for neighbor in current_node.neighbors]
            
            # Visit neighbors
            for neighbor in current_node.neighbors:
                if neighbor.val not in visited:
                    dfs(neighbor)
        
        dfs(node)
        return result
    
    # Create original graph and clone it
    original_graph = create_graph_from_adj_list(adj_list)
    solution = Solution()
    cloned_graph = solution.cloneGraph(original_graph)
    
    # Convert cloned graph back to adjacency list
    result_adj_list = graph_to_adj_list(cloned_graph)
    
    print(f"{test_name}:")
    print(f"  Input: {adj_list}")
    print(f"  Expected: {expected_adj_list}")
    print(f"  Got: {result_adj_list}")
    print(f"  Pass: {result_adj_list == expected_adj_list}")
    print()

# Run test cases
run_clone_graph_test([[2,4],[1,3],[2,4],[1,3]], [[2,4],[1,3],[2,4],[1,3]], "Example 1: Simple cycle graph")
run_clone_graph_test([[]], [[]], "Example 2: Single node with no neighbors")
run_clone_graph_test([], [], "Example 3: Empty graph")
run_clone_graph_test([[2],[1]], [[2],[1]], "Edge case: Two nodes connected")
run_clone_graph_test([[2,3],[1,3],[1,2]], [[2,3],[1,3],[1,2]], "Edge case: Triangle")
run_clone_graph_test([[2,3,4],[1,3,4],[1,2,4],[1,2,3]], [[2,3,4],[1,3,4],[1,2,4],[1,2,3]], "Edge case: Complete graph of 4 nodes")
run_clone_graph_test([[2],[1,3],[2,4],[3]], [[2],[1,3],[2,4],[3]], "Edge case: Linear graph")
run_clone_graph_test([[2,3],[1,4],[1,4],[2,3]], [[2,3],[1,4],[1,4],[2,3]], "Edge case: Bipartite graph")