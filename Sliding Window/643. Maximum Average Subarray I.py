class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        max_output = sum(nums[:k]) * 1.0 / k
        current_sum = max_output * k
        
        for index in range(k, len(nums)):
            current_sum = current_sum - nums[index - k] + nums[index]
            max_output = max(max_output, current_sum * 1.0 / k)

        return max_output