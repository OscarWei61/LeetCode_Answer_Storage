class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        direction = [(0, 1), (0, 0), (1, 1), (1, 0)]

        queue = deque()
        fresh = 0
        
        row = len(grid)
        cols = len(grid[0])

        for r in range(row):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh = fresh + 1
        
        if fresh == 0:
            return 0
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        minutes = 0

        while queue:
            r, c, minutes = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
            
                if 0 <= nr < row and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh = fresh - 1
                    queue.append((nr, nc, minutes + 1))

        if fresh == 0:
        
            return minutes
        
        else:
            return -1
