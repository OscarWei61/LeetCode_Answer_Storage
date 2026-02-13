class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
            
        left_point = 0
        right_point = 0
        result = []

        for n_index in range(len(nums) - 1):
            if nums[n_index] != nums[n_index + 1] - 1:
                if left_point == right_point:
                    result.append(str(nums[n_index])) 
                else:
                    result.append(str(str(nums[left_point]) + "->" + str(nums[n_index])))
                left_point = n_index + 1
                right_point = n_index + 1
            else:
                right_point = right_point + 1
        
        last_index = len(nums) - 1
        
        if left_point == last_index:
            result.append(str(nums[last_index]))
        else:
            result.append(str(nums[left_point]) + "->" + str(nums[last_index]))
        return result 

