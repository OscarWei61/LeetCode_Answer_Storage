class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        if k == 1:
            return 0
        
        nums.sort()
        mini_difference = float('inf')

        for index in range(len(nums) - k + 1):
            mini_difference = min(mini_difference, nums[index + k - 1] - nums[index])
        
        return mini_difference