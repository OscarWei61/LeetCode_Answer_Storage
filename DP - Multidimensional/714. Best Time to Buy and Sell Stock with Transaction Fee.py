class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        if not prices:
            return 0 

        hold = -prices[0]
        cash = 0

        for price in prices[1:]:
            hold = max(hold, cash - price)
            cash = max(cash, price + hold - fee)
        
        return cash