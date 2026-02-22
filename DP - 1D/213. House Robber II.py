class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        def rob(houses):
            prev_max, current_max = 0, 0
            for num in houses:
                new_max = max(current_max, prev_max + num)
                prev_max = current_max
                current_max = new_max
            return current_max
        
        result1 = rob(nums[1:])
        result2 = rob(nums[:-1])

        return max(result1, result2)