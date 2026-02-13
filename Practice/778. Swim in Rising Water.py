class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        n = len(grid)
        visited = set()
        heap = [(grid[0][0], 0, 0)]
        visited.add((0, 0))
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        max_height = 0

        while heap:
            h, x, y = heapq.heappop(heap)

            max_height = max(max_height, h)

            if x == n - 1 and y == n - 1:
                return max_height
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    heapq.heappush(heap, (grid[nx][ny], nx, ny))

        return max_height