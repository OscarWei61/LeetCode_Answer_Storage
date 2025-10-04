class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        steps = [[0] * n for _ in range(m)]

        for index in range(n):
            steps[0][index] = 1

        for index in range(m):
            steps[index][0] = 1

        for index_m in range(1, n):
            for index_n in range(1, m):
                steps[index_n][index_m] = steps[index_n][index_m] + steps[index_n - 1][index_m] + steps[index_n][index_m - 1]

        return steps[-1][-1]