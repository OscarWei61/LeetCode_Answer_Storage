class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0

        for index in range(0, len(nums)):
            result = result ^ nums[index]

        return result