class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        farthest = 0

        for index in range(len(nums)):
            if index > farthest:
                return False
            farthest = max(farthest, index + nums[index])
        
        return True