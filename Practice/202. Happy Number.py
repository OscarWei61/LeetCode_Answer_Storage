class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_total(num):
            total_sum = 0
            while num > 0:
                digit = num % 10
                total_sum += digit * digit
                num //= 10
            return total_sum
        
        seen_num = set()

        while n != 1 and n not in seen_num:
            if n not in seen_num:
                seen_num.add(n)
            else:
                return False
            n = get_total(n)
        if n != 1:
            return False
        else:
            return True