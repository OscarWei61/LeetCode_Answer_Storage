class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited_set = set()
        left_index = 0

        for right_index in range(len(nums)):
            if nums[right_index] not in visited_set:
                visited_set.add(nums[right_index])
                nums[left_index] = nums[right_index]
                left_index = left_index + 1
            
        return left_index