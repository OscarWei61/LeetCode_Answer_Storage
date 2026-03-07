class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for index in range(coin, amount + 1):
                dp[index] = dp[index] + dp[index - coin]
        
        return dp[amount]