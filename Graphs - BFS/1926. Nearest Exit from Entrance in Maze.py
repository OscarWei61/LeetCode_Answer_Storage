class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        m, n = len(maze), len(maze[0])
        q = deque([(entrance[0], entrance[1], 0)])
        visited = set()
        visited.add((entrance[0], entrance[1]))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while q:
            r, c, steps = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == "." and (nr, nc) not in visited:
                    if (nr in [0, m-1] or nc in [0, n-1]) and [nr, nc] != entrance:
                        return steps + 1
                    visited.add((nr, nc))
                    q.append((nr, nc, steps + 1))
        
        return -1