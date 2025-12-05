class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        count = 0
        left_sum = 0

        for index in range(len(nums) - 1):
            left_sum = left_sum + nums[index]
            total_sum = total_sum - nums[index]

            if (total_sum - left_sum) % 2 == 0:
                count = count + 1
            
        return count