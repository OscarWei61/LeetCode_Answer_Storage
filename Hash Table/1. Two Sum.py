class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Better solution using hash table
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i

        '''
        for num1 in range(0, len(nums)):
            for num2 in range(num1+1, len(nums)):
                if nums[num1] + nums[num2] == target:
                    return [num1, num2]
        '''

solution = Solution()
print(solution.twoSum([2,7,11,15], 13))