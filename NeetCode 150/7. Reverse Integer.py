class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX_INT = 2 ** 31 - 1
        MIN_INT = - 2 ** 31

        result = 0
        
        if x > 0:
            sign = 1
        else:
            sign = -1

        x = abs(x)

        while x != 0:
            last_digit = x % 10
            x = x // 10

            if result > (MAX_INT - last_digit) / 10:
                return 0

            result = result * 10 + last_digit
        
        result = result * sign

        if result > MAX_INT or result < MIN_INT:
            return 0

        return result

