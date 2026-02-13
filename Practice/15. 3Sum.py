class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        result = []

        for index in range(len(nums) - 2):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            
            left_point = index + 1
            right_point = len(nums) - 1

            while left_point < right_point:
                total = nums[left_point] + nums[index] + nums[right_point]

                if total < 0:
                    left_point = left_point + 1

                elif total > 0:
                    right_point = right_point - 1

                else:
                    result.append([nums[index], nums[left_point], nums[right_point]])
                    
                    while left_point < right_point and nums[left_point] == nums[left_point + 1]:
                        left_point = left_point + 1
                    
                    while left_point < right_point and nums[right_point] == nums[right_point - 1]:
                        right_point = right_point - 1

                    left_point = left_point + 1
                    right_point = right_point - 1
        
        return result