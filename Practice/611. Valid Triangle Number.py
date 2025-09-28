class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        count = 0

        for max_value in range(n - 1, 1, -1):
            i = 0
            j = max_value - 1

            while i < j:
                if nums[i] + nums[j] > nums[max_value]:
                    count = count + (j - i)
                    j = j - 1
                
                else:
                    i = i + 1
            
        return count