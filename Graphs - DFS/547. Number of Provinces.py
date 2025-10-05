class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = [False] * n

        def dfs(i):
            for j in range(n):
                if isConnected[i][j] == 1 and not visited[j]:
                    visited[j] = True
                    dfs(j)

        how_many_cities = 0

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                how_many_cities = how_many_cities + 1
        
        return how_many_cities