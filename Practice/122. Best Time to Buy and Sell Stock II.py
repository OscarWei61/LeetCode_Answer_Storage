class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0

        for price_index in range(1, len(prices)):
            if prices[price_index] > prices[price_index - 1]:
                profit = profit + prices[price_index] - prices[price_index - 1]

        return profit