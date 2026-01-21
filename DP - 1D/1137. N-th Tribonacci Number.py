class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        t_sum = 0
        item = [0, 1, 1]
        
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        for index in range(3, n + 1):
            t_sum = item[0] + item[1] + item[2]
            item[0] = item[1]
            item[1] = item[2]
            item[2] = t_sum
        
        return t_sum