class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_map = {}

        for index in range(len(nums)):
            if nums[index] not in nums_map:
                nums_map[nums[index]] = index
            else:
                if index - nums_map[nums[index]] <= k:
                    return True
                else:
                    nums_map[nums[index]] = index
        
        return False
