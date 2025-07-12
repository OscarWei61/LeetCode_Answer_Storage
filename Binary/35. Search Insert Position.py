class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left_index = 0
        right_index = len(nums) - 1
        while(left_index <= right_index):
            mid_index = (left_index + right_index) / 2
            if nums[mid_index] < target:
                left_index = mid_index + 1

            elif nums[mid_index] > target:
                right_index = mid_index - 1
            
            elif nums[mid_index] == target:
                return mid_index

        if mid_index == 0:
            if nums[mid_index] > target:
            
                return 0
            else :
                return mid_index + 1
        
        if mid_index == (len(nums) - 1):
            if nums[mid_index] > target:
            
                return mid_index
            else :
                return mid_index + 1      

        if mid_index == right_index or mid_index == left_index:
            
            if nums[mid_index] > target:
            
                return mid_index
            else :
                return mid_index + 1              
            

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left_index, right_index = 0, len(nums) - 1
        
        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2
            if nums[mid_index] == target:
                return mid_index
            elif nums[mid_index] < target:
                left_index = mid_index + 1
            else:
                right_index = mid_index - 1
        
        return left_index
