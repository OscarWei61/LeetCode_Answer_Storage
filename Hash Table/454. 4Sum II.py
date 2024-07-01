
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        
        total_count_zeros = 0
        count_map = {}

        for num1 in nums1:
            for num2 in nums2:
                pair_sum = num1 + num2
                if pair_sum in count_map:
                    count_map[pair_sum] += 1
                else:
                    count_map[pair_sum] = 1

        for num3 in nums3:
            for num4 in nums4:
                pair_sum = num3 + num4
                if -pair_sum in count_map:
                    total_count_zeros += count_map[-pair_sum]

        return total_count_zeros