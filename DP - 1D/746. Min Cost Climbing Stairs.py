class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost_list = [0] * len(cost)
        cost_list[0] = cost[0]
        cost_list[1] = cost[1]

        for index in range(2, len(cost)):
            cost_list[index] = min(cost_list[index - 1], cost_list[index - 2]) + cost[index]
        
        return min(cost_list[-1], cost_list[-2])
