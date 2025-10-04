class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_index = 0
        right_index = len(nums) - 1

        while left_index < right_index:
            mid_index = (left_index + right_index) // 2

            if nums[mid_index] < nums[mid_index + 1]:
                left_index = mid_index + 1
            else:
                right_index = mid_index

        return left_index