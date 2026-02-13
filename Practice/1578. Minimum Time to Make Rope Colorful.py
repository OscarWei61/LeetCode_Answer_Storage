class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        total_time = 0
        max_time_in_group = neededTime[0]

        for index in range(1, len(colors)):
            if colors[index] == colors[index - 1]:
                total_time = total_time + min(max_time_in_group, neededTime[index])
                max_time_in_group = max(max_time_in_group, neededTime[index])
            else:
                max_time_in_group = neededTime[index]
        
        return total_time
           

        