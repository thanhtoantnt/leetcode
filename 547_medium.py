from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0
        
        def dfs(city):
            """
            Depth-First Search to mark all connected cities as visited
            """
            visited[city] = True
            # Check all other cities to see if they're connected to current city
            for neighbor in range(n):
                # If connected and not visited, explore recursively
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)
        
        # Iterate through all cities
        for city in range(n):
            if not visited[city]:
                provinces += 1
                dfs(city)  # Mark all cities in this province as visited
        
        return provinces