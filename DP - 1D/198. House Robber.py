class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums)

        prev_rob = nums[0]
        second_rob = max(nums[0], nums[1])

        for n in range(2, len(nums)):
            new_rob = max(prev_rob + nums[n], second_rob)
            prev_rob, second_rob = second_rob, new_rob
        
        return max(prev_rob, second_rob)
