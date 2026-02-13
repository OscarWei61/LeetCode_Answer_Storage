class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        current_total = 0
        for index in range(k):
            current_total = current_total + nums[index]
        
        max_total = current_total

        for index in range(k, len(nums)):
            
            current_total = current_total - nums[index - k] + nums[index]
            max_total = max(max_total, current_total)
        
        return float(max_total) / k
        