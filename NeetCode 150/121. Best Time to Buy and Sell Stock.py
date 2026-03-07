class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest_price = float('inf')
        max_price = float('-inf')
        current_profit = 0

        for p in prices:
            lowest_price = min(lowest_price, p)
            current_profit = max(current_profit, p - lowest_price)
        
        return current_profit