from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Returns the order of courses to finish all courses given prerequisites.
        
        Problem Understanding:
        - There are numCourses courses to take, labeled from 0 to numCourses - 1
        - Given prerequisites where prerequisites[i] = [ai, bi] means to take course ai,
          you must first take course bi
        - Return the ordering of courses to finish all courses
        - If impossible (cycle exists), return empty array
        
        Approach:
        - Model as a directed graph where each course is a node
        - An edge from bi to ai represents "bi is prerequisite for ai"
        - Use topological sort with DFS
        - If a cycle is detected, return empty array
        - Otherwise, return courses in reverse order of DFS finishing times
        
        Time Complexity: O(V + E) where V is number of courses and E is number of prerequisites
        Space Complexity: O(V + E) for adjacency list and visited array
        
        Args:
            numCourses: Number of courses to take
            prerequisites: List of prerequisite pairs [course, prerequisite]
            
        Returns:
            List representing valid course order, or empty list if impossible
        """
        # Build adjacency list representation of the graph
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)  # prereq -> course
        
        # States: 0 = unvisited, 1 = visiting (in current DFS path), 2 = visited
        state = [0] * numCourses
        result = []
        
        def dfs(course):
            """DFS helper to detect cycles and build result in reverse order"""
            if state[course] == 1:  # Currently in this DFS path - cycle detected
                return False
            if state[course] == 2:  # Already processed - no need to process again
                return True
            
            # Mark as visiting (part of current DFS path)
            state[course] = 1
            
            # Check all neighbors (courses that depend on this course)
            for next_course in graph[course]:
                if not dfs(next_course):
                    return False  # Cycle detected
            
            # Mark as visited (fully processed)
            state[course] = 2
            # Add to result after processing all dependencies
            result.append(course)
            return True
        
        # Process each unvisited course
        for i in range(numCourses):
            if state[i] == 0:  # Unvisited
                if not dfs(i):
                    return []  # Cycle detected, return empty array
        
        # Reverse the result to get correct topological order
        return result[::-1]

def run_course_schedule_2_test(numCourses, prerequisites, expected, test_name):
    """
    Tests the findOrder function.
    
    Args:
        numCourses: Number of courses
        prerequisites: List of prerequisite pairs
        expected: Expected course order (any valid order is acceptable)
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.findOrder(numCourses, prerequisites)
    
    # Verify result is valid by checking if it's a permutation of all courses and satisfies prerequisites
    def is_valid_result(result, numCourses, prerequisites):
        if len(result) != numCourses:
            return False
        if set(result) != set(range(numCourses)):
            return False
        
        # Create a position map for courses in result
        pos = {course: i for i, course in enumerate(result)}
        
        # Check if all prerequisites are satisfied
        for course, prereq in prerequisites:
            if pos.get(prereq, -1) >= pos.get(course, float('inf')):
                return False  # Prereq comes after course in result
        return True
    
    is_valid = is_valid_result(result, numCourses, prerequisites)
    expected_is_empty = len(expected) == 0
    result_is_empty = len(result) == 0
    
    print(f"{test_name}:")
    print(f"  Input: numCourses = {numCourses}, prerequisites = {prerequisites}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Is valid: {is_valid}")
    print(f"  Pass: {(expected_is_empty and result_is_empty) or (not expected_is_empty and is_valid)}")
    print()

# Run test cases
run_course_schedule_2_test(2, [[1,0]], [0,1], "Example 1: 2 courses, [1,0] -> [0,1]")
run_course_schedule_2_test(4, [[1,0],[2,0],[3,1],[3,2]], [0,1,2,3], "Example 2: 4 courses with dependencies -> [0,1,2,3] or similar")
run_course_schedule_2_test(1, [], [0], "Example 3: 1 course, no prerequisites -> [0]")
run_course_schedule_2_test(2, [[1,0],[0,1]], [], "Edge case: 2 courses, [1,0],[0,1] -> [] (cycle)")
run_course_schedule_2_test(3, [[1,0],[2,0],[2,1]], [0,1,2], "Edge case: 3 courses, linear dependencies -> [0,1,2]")
run_course_schedule_2_test(4, [[2,0],[1,0],[3,1],[3,2],[1,3]], [], "Edge case: Complex cycle -> []")
run_course_schedule_2_test(5, [[1,0],[2,1],[3,2],[4,3]], [0,1,2,3,4], "Edge case: Linear chain of 5 courses -> [0,1,2,3,4]")
run_course_schedule_2_test(3, [[0,1],[1,2],[2,0]], [], "Edge case: Simple 3-node cycle -> []")
run_course_schedule_2_test(4, [[0,1],[1,2],[2,3]], [3,2,1,0], "Edge case: Linear 4-node chain -> [3,2,1,0] or similar")
run_course_schedule_2_test(0, [], [], "Edge case: 0 courses -> []")