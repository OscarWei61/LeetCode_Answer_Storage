class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if (price - min_price) > max_profit:
                max_profit = (price - min_price)
            if price < min_price:
                min_price = price

        return max_profit

s = Solution()
s.maxProfit([7,1,5,3,6,4])