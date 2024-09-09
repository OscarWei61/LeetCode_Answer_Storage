class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        cal_list1 = [0] * len(nums)
        cal_list1[0] = nums[0]
        cal_list1[1] = max(cal_list1[0], nums[1])

        cal_list2 = [0] * len(nums)
        cal_list2[0] = 0
        cal_list2[1] = nums[1]

        for index in range(2, len(nums)):
            if index == (len(nums) - 1):
                cal_list1[index] = cal_list1[index - 1]
            else:
                cal_list1[index] = max(cal_list1[index - 1], cal_list1[index - 2] + nums[index])
            
            cal_list2[index] = max(cal_list2[index - 1], cal_list2[index - 2] + nums[index])
        
        return max(cal_list1[-1], cal_list2[-1])

