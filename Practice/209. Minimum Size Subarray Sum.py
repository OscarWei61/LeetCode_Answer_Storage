class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        left_point = 0
        current_total = 0
        min_length = float('inf')

        for right_point in range(0, len(nums)):
            current_total = current_total + nums[right_point]

            while current_total >= target:
                min_length = min(min_length, right_point - left_point + 1)
                current_total = current_total - nums[left_point]
                left_point = left_point + 1
        
        if min_length == float('inf'):
            return 0  
        else:
            return min_length