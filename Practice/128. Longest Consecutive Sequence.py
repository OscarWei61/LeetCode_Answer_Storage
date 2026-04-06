class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums_map = set(nums)
        max_length = 0
        count_length = 0

        for n in nums_map:
            
            if n - 1 not in nums_map:
                count = n
                count_length = 1

                while count + 1 in nums_map:
                    count_length = count_length + 1
                    count = count + 1
                
                max_length = max(max_length, count_length)
        
        return max_length