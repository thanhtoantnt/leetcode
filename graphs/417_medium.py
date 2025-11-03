from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Finds cells from which water can flow to both Pacific and Atlantic oceans.
        
        Problem Understanding:
        - Given a grid of heights representing an island
        - Pacific Ocean borders the top and left edges
        - Atlantic Ocean borders the bottom and right edges
        - Water flows from higher to lower (or equal) height in 4 directions
        - Find cells from which water can reach both oceans
        
        Approach:
        - Use reverse thinking: instead of finding where water flows from each cell
        - Start from ocean edges and find all cells that can reach the ocean
        - Use DFS/BFS from all Pacific border cells and all Atlantic border cells
        - Find intersection of cells reachable from both oceans
        
        Time Complexity: O(M * N) where M and N are grid dimensions
        Space Complexity: O(M * N) for visited arrays and result
        
        Args:
            heights: 2D grid of heights
            
        Returns:
            List of coordinates where water can reach both oceans
        """
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        
        # Create boolean matrices to track reachable cells from each ocean
        pacific_reachable = [[False] * n for _ in range(m)]
        atlantic_reachable = [[False] * n for _ in range(m)]
        
        def dfs(row, col, reachable):
            """DFS to find all cells that can reach the given ocean"""
            reachable[row][col] = True
            
            # Check all 4 directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check bounds, if not visited, and if water can flow from new cell to current cell
                # (reverse direction: water flows from higher/equal to lower)
                if (0 <= new_row < m and 0 <= new_col < n and 
                    not reachable[new_row][new_col] and 
                    heights[new_row][new_col] >= heights[row][col]):
                    dfs(new_row, new_col, reachable)
        
        # Start DFS from all Pacific border cells (top row and left column)
        for i in range(m):
            dfs(i, 0, pacific_reachable)  # Left edge
        for j in range(n):
            dfs(0, j, pacific_reachable)  # Top edge
        
        # Start DFS from all Atlantic border cells (bottom row and right column)
        for i in range(m):
            dfs(i, n - 1, atlantic_reachable)  # Right edge
        for j in range(n):
            dfs(m - 1, j, atlantic_reachable)  # Bottom edge
        
        # Find cells that can reach both oceans
        result = []
        for i in range(m):
            for j in range(n):
                if pacific_reachable[i][j] and atlantic_reachable[i][j]:
                    result.append([i, j])
        
        return result

def run_pacific_atlantic_test(heights, expected, test_name):
    """
    Tests the pacificAtlantic function.
    
    Args:
        heights: Input 2D grid of heights
        expected: Expected list of coordinates
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.pacificAtlantic(heights)
    
    # Convert to sets of tuples for order-independent comparison
    result_set = set(tuple(coord) for coord in result)
    expected_set = set(tuple(coord) for coord in expected)
    
    print(f"{test_name}:")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result_set == expected_set}")
    print(f"  Count: Expected {len(expected)}, Got {len(result)}")
    print()

# Run test cases
run_pacific_atlantic_test(
    [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ],
    [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]],
    "Example 1: Complex grid -> [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]"
)

run_pacific_atlantic_test(
    [[1]],
    [[0,0]],
    "Example 2: Single cell -> [[0,0]]"
)

run_pacific_atlantic_test(
    [
        [1,2,3],
        [8,9,4],
        [7,6,5]
    ],
    [[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]],
    "Edge case: Peak in center -> All cells can reach both oceans"
)

run_pacific_atlantic_test(
    [
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ],
    [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]],
    "Edge case: All same height -> All cells can reach both oceans"
)

run_pacific_atlantic_test(
    [
        [10,10,10],
        [10,1,10],
        [10,10,10]
    ],
    [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]],
    "Edge case: Low center -> All cells can reach both oceans"
)

run_pacific_atlantic_test(
    [
        [1,2,3,4],
        [12,13,14,5],
        [11,16,15,6],
        [10,9,8,7]
    ],
    [[0,3],[1,0],[1,3],[2,0],[2,3],[3,0],[3,1],[3,2],[3,3]],
    "Edge case: Spiral pattern"
)

run_pacific_atlantic_test(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ],
    [[0,2],[1,2],[2,0],[2,1],[2,2]],
    "Edge case: Ascending grid"
)

run_pacific_atlantic_test(
    [
        [9,8,7],
        [6,5,4],
        [3,2,1]
    ],
    [[0,0],[0,1],[0,2],[1,0],[2,0]],
    "Edge case: Descending grid"
)