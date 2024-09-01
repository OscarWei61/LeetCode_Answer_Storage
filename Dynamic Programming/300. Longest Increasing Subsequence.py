class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cal_list = [1] * len(nums)

        for right_index in range(1, len(nums)):
            for left_index in range(0, right_index):
                if nums[left_index] < nums[right_index]:
                    cal_list[right_index] = max(cal_list[left_index] + 1, cal_list[right_index])

        return max(cal_list)
    
