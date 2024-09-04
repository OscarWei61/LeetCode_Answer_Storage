class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        cal_list = [0] * (amount + 1)

        for coin in coins:
            for index in range(coin, amount + 1):
                cal_list[index] = min(cal_list[index - 1] + 1, amount / coin)
            
        return cal_list[-1]
        
