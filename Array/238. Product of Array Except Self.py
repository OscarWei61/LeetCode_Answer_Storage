class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1] * len(nums)
        left_muliple_result = 1
        right_multiple_result = 1

        for index in range(len(nums)):
            answer[index] = left_muliple_result
            left_muliple_result = left_muliple_result * nums[index]

        for index in range(len(nums) - 1, -1, -1):
            answer[index] = right_multiple_result * answer[index]
            right_multiple_result = right_multiple_result * nums[index]
        
        return answer