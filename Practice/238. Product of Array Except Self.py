class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1] * len(nums)
        left_multiple = 1
        right_multiple = 1

        for index in range(0, len(nums)):
            answer[index] = answer[index] * left_multiple
            left_multiple = left_multiple * nums[index]
        
        for index in range(len(nums) - 1, -1, -1):
            answer[index] = answer[index] * right_multiple
            right_multiple = right_multiple * nums[index]
        
        return answer