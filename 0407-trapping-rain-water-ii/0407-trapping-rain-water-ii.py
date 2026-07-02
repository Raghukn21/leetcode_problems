import heapq

class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        pq = []
        
        # Add all boundary cells to the min-heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(pq, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        water_trapped = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while pq:
            height, r, c = heapq.heappop(pq)
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    # Water is trapped if the neighbor is lower than the current boundary height
                    water_trapped += max(0, height - heightMap[nr][nc])
                    
                    # Push the neighbor into the heap with the updated effective height
                    heapq.heappush(pq, (max(height, heightMap[nr][nc]), nr, nc))
                    visited[nr][nc] = True
                    
        return water_trapped