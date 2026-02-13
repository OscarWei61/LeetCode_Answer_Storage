class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)

        for index in range(len(nums) - 2):
            if nums[index + 1] + nums[index + 2] > nums[index]:
                return nums[index + 1] + nums[index + 2] + nums[index]

        return 0