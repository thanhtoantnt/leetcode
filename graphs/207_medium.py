from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Determines if it's possible to finish all courses given prerequisites.
        
        Problem Understanding:
        - There are numCourses courses to take, labeled from 0 to numCourses - 1
        - Given prerequisites where prerequisites[i] = [ai, bi] means to take course ai,
          you must first take course bi
        - Return True if it's possible to finish all courses, False otherwise
        - This is essentially detecting cycles in a directed graph
        
        Approach:
        - Model as a directed graph where each course is a node
        - An edge from bi to ai represents "bi is prerequisite for ai"
        - Use DFS with three states: unvisited, visiting, visited
        - If we encounter a node in "visiting" state during DFS, there's a cycle
        - If no cycles exist, it's possible to finish all courses
        
        Time Complexity: O(V + E) where V is number of courses and E is number of prerequisites
        Space Complexity: O(V + E) for adjacency list and visited array
        
        Args:
            numCourses: Number of courses to take
            prerequisites: List of prerequisite pairs [course, prerequisite]
            
        Returns:
            True if all courses can be finished, False otherwise
        """
        # Build adjacency list representation of the graph
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)  # prereq -> course
        
        # States: 0 = unvisited, 1 = visiting (in current DFS path), 2 = visited
        state = [0] * numCourses
        
        def has_cycle(course):
            """DFS helper to detect cycles starting from given course"""
            if state[course] == 1:  # Currently in this DFS path - cycle detected
                return True
            if state[course] == 2:  # Already processed - no cycle from here
                return False
            
            # Mark as visiting (part of current DFS path)
            state[course] = 1
            
            # Check all neighbors (courses that depend on this course)
            for next_course in graph[course]:
                if has_cycle(next_course):
                    return True
            
            # Mark as visited (fully processed)
            state[course] = 2
            return False
        
        # Check for cycles starting from each unvisited course
        for i in range(numCourses):
            if state[i] == 0:  # Unvisited
                if has_cycle(i):
                    return False  # Cycle detected, can't finish all courses
        
        return True  # No cycles detected, can finish all courses

def run_course_schedule_test(numCourses, prerequisites, expected, test_name):
    """
    Tests the canFinish function.
    
    Args:
        numCourses: Number of courses
        prerequisites: List of prerequisite pairs
        expected: Expected result (True/False)
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.canFinish(numCourses, prerequisites)
    
    print(f"{test_name}:")
    print(f"  Input: numCourses = {numCourses}, prerequisites = {prerequisites}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_course_schedule_test(2, [[1,0]], True, "Example 1: 2 courses, [1,0] -> True")
run_course_schedule_test(2, [[1,0],[0,1]], False, "Example 2: 2 courses, [1,0],[0,1] -> False (cycle)")
run_course_schedule_test(1, [], True, "Example 3: 1 course, no prerequisites -> True")
run_course_schedule_test(3, [[1,0],[2,0],[2,1]], True, "Edge case: 3 courses, linear dependencies -> True")
run_course_schedule_test(4, [[2,0],[1,0],[3,1],[3,2],[1,3]], False, "Edge case: Complex cycle -> False")
run_course_schedule_test(5, [[1,0],[2,1],[3,2],[4,3]], True, "Edge case: Linear chain of 5 courses -> True")
run_course_schedule_test(3, [[0,1],[1,2],[2,0]], False, "Edge case: Simple 3-node cycle -> False")
run_course_schedule_test(4, [[0,1],[1,2],[2,3]], True, "Edge case: Linear 4-node chain -> True")
run_course_schedule_test(4, [[0,1],[2,1],[3,2],[1,3]], False, "Edge case: Circular dependency -> False")
run_course_schedule_test(0, [], True, "Edge case: 0 courses -> True")
run_course_schedule_test(1, [[0,0]], False, "Edge case: Self-prerequisite -> False")
run_course_schedule_test(3, [[0,1],[1,2]], True, "Edge case: Two prerequisites -> True")