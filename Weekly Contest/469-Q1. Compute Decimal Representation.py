class Solution(object):
    def decimalRepresentation(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        result = []
        factor = 1
        
        while n > 0:
            digit = n % 10
            if digit != 0:
                result.append(digit * factor)
            n = n // 10
            factor = factor * 10
            
        return result[::-1]