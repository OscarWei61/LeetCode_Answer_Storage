class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        max_reach = 0

        for index, num in enumerate(nums):
            if index > max_reach:
                return False
            
            max_reach = max(max_reach, index + num)
        
        return True

        '''
        if not nums:
            return False
        if len(nums) == 1:
            return True

        cal_list = [False] * (len(nums) + 1)
        cal_list[0] = True

        for index in range(0, len(nums)):
            for num_index in range(0, nums[index] + 1):
                if index + num_index <= len(nums):
                    if cal_list[index] == True:
                        cal_list[index + num_index] = True

                if cal_list[len(nums) - 1] == True:
                    return True
            
        return False
        '''