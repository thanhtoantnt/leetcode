from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Finds the k closest points to the origin (0, 0).
        
        Problem Understanding:
        - Given an array of points on the X-Y plane and integer k
        - Return the k closest points to the origin
        - Distance calculated using Euclidean distance formula
        - Need to return actual points, not just distances
        
        Approach:
        - Use max-heap to keep track of k closest points seen so far
        - For each point, calculate its squared distance to origin (avoid sqrt for efficiency)
        - If heap size < k, add point
        - If heap size == k and current point is closer than max in heap, replace it
        - Use negative distances for max-heap behavior with Python's min-heap
        
        Time Complexity: O(n * log k) where n is number of points
        Space Complexity: O(k) for the heap
        
        Args:
            points: List of [x, y] coordinates
            k: Number of closest points to return
            
        Returns:
            List of k closest points to origin
        """
        # Max-heap to store k closest points (using negative distances for max-heap behavior)
        max_heap = []
        
        for point in points:
            x, y = point[0], point[1]
            # Calculate squared distance (no need to take sqrt, preserves ordering)
            dist_squared = x * x + y * y
            
            if len(max_heap) < k:
                # If heap not full, add the point (with negative distance for max-heap)
                heapq.heappush(max_heap, (-dist_squared, point))
            else:
                # If heap is full and current point is closer than farthest in heap
                if dist_squared < -max_heap[0][0]:
                    # Remove farthest and add current point
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (-dist_squared, point))
        
        # Extract points from heap (ignore distances)
        result = [point for _, point in max_heap]
        return result

def run_k_closest_test(points, k, expected, test_name):
    """
    Tests the kClosest function.
    
    Args:
        points: List of [x, y] coordinates
        k: Number of closest points to return
        expected: Expected k closest points
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.kClosest(points, k)
    
    # Convert to sets of tuples for order-independent comparison
    result_set = set(tuple(point) for point in result)
    expected_set = set(tuple(point) for point in expected)
    
    print(f"{test_name}:")
    print(f"  Input: points = {points}, k = {k}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result_set == expected_set}")
    print(f"  Count: Expected {len(expected)}, Got {len(result)}")
    print()

# Run test cases
run_k_closest_test([[1,1],[-1,-1],[3,4]], 2, [[1,1],[-1,-1]], "Example 1: [[1,1],[-1,-1],[3,4]], k=2 -> [[1,1],[-1,-1]]")
run_k_closest_test([[3,3],[5,-1],[-2,4]], 2, [[3,3],[-2,4]], "Example 2: [[3,3],[5,-1],[-2,4]], k=2 -> [[3,3],[-2,4]]")
run_k_closest_test([[0,1],[1,0]], 2, [[0,1],[1,0]], "Edge case: [[0,1],[1,0]], k=2 -> [[0,1],[1,0]]")
run_k_closest_test([[1,1]], 1, [[1,1]], "Edge case: Single point, k=1 -> [[1,1]]")
run_k_closest_test([[0,0],[1,1],[2,2],[3,3]], 2, [[0,0],[1,1]], "Edge case: [[0,0],[1,1],[2,2],[3,3]], k=2 -> [[0,0],[1,1]]")
run_k_closest_test([[-5,4],[4,6],[-6,-5],[7,8]], 2, [[-5,4],[4,6]], "Edge case: Mixed quadrants -> [[-5,4],[4,6]]")
run_k_closest_test([[1,3],[-2,2]], 1, [[-2,2]], "Edge case: [[1,3],[-2,2]], k=1 -> [[-2,2]]")
run_k_closest_test([[6,10],[-3,3],[-2,5],[0,2]], 3, [[0,2],[-3,3],[-2,5]], "Edge case: [[6,10],[-3,3],[-2,5],[0,2]], k=3 -> [[0,2],[-3,3],[-2,5]]")