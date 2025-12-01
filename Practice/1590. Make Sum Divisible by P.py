class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        n = len(nums)
        min_len = len(nums)

        if sum(nums) % p == 0:
            return 0
        
        total_sum = sum(nums)
        remaining = total_sum % p

        prefix_mod_map = {0: -1}
        current_prefix_sum_mod = 0

        for index, num in enumerate(nums):
            current_prefix_sum_mod = (current_prefix_sum_mod + num) % p
            m_target = (current_prefix_sum_mod - remaining + p) % p
            
            if m_target in prefix_mod_map:
                j = prefix_mod_map[m_target]
                min_len = min(min_len, index - j)
            
            prefix_mod_map[current_prefix_sum_mod] = index
            
        
        return min_len if min_len < n else -1