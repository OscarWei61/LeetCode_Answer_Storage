class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        guard_set = set(map(tuple, guards))
        wall_set = set(map(tuple, walls))
        guarded = set()

        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        
        for gx, gy in guards: 
            for dx, dy in direction:
                x = gx + dx
                y = gy + dy
                
                while 0 <= x < m and 0 <= y < n:
                    if (x, y) in wall_set or (x, y) in guard_set:
                        break
                    
                    guarded.add((x, y))
                    x = x + dx
                    y = y + dy
                
        return m * n - len(guard_set) - len(wall_set) - len(guarded)