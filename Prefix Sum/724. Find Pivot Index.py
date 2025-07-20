class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        left_sum = 0

        for index in range(0, len(nums)):
            if left_sum == (total_sum - left_sum - nums[index]):
                return index
            
            left_sum = left_sum + nums[index]
        
        return -1
        