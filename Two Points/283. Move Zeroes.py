class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        
        read_index = 0 
        write_index = 0

        for read_index in range(0, len(nums)):
            if nums[read_index] != 0:
                nums[write_index] = nums[read_index]
                write_index = write_index + 1
            
        for index in range(write_index, len(nums)):
            nums[index] = 0
        
        return nums
