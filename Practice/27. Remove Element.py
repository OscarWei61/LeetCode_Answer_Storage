class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left_index = 0

        for right_index in range(len(nums)):
            if nums[right_index] != val:
                nums[left_index] = nums[right_index]
                left_index = left_index + 1
            
        return left_index