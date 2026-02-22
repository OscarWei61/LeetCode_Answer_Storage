class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor_sum = 0

        for n in nums:
            xor_sum = xor_sum ^ n
        
        difference = xor_sum & -xor_sum
        a = 0
        b = 0

        for n in nums:
            if n & difference:
                a = a ^ n
            else:
                b = b ^ n
        
        return [a, b]