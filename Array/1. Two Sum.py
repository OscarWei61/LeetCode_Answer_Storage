class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dic = {}
        for index,num in enumerate(nums):
            complement = target - num

            if complement in nums_dic:
                return [nums_dic[complement],index]
            
            nums_dic[num] = index