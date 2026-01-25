class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0: 
            return 1
        
        if n == 1: 
            return 1
        
        if n == 2: 
            return 2
        
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2

        for index in range(3, n + 1):
            dp[index] = (2 * dp[index - 1] + dp[index - 3]) % (10**9 + 7)

        return dp[n]