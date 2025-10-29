class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        total_flips = 0
        while a > 0 or b > 0 or c > 0:
            a_bit = a & 1
            b_bit = b & 1
            c_bit = c & 1

            if c_bit == 1:

                if (a_bit | b_bit) == 0:
                    total_flips = total_flips + 1
            
            else:
                total_flips = total_flips + a_bit + b_bit

            a >>= 1
            b >>= 1
            c >>= 1

        return total_flips