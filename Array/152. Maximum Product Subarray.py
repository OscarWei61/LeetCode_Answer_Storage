class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        current_max = current_min = result = nums[0]
        for num in nums[1:]:
            temp = max(num, current_max * num, current_min * num)
            current_min = min(num, current_max * num, current_min * num)
            current_max = temp
            result = max(current_max, result)
        
        return result