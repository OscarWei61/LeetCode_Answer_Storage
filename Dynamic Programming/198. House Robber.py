class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        cal_list = [0] * len(nums)
        cal_list[0] = nums[0]
        cal_list[1] = max(nums[0], nums[1])

        for index in range(2, len(nums)):
            cal_list[index] = max(cal_list[index - 1], cal_list[index - 2] + nums[index])

        return cal_list[-1]