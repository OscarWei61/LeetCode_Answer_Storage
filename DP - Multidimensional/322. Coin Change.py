class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for index in range(1, amount + 1):
            for coin in coins:
                if index - coin >= 0:
                    dp[index] = min(dp[index], dp[index - coin] + 1)

        if dp[amount] != float('inf'):
            return dp[amount] 
        else:
            return -1