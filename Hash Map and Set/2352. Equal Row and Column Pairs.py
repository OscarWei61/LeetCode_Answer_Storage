class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        row_count = {}

        for row in grid:
            t = tuple(row)
            if t in row_count:
                row_count[t] = row_count[t] + 1
            else:
                row_count[t] = 1

        result = 0

        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            if col in row_count:
                result = row_count[col] + result

        return result 