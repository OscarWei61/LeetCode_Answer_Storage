class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def count_total(num):
            total = 0
            while num != 0:
                digit = num % 10 
                total = total + digit ** 2
                num = num // 10

            return total
        
        visited = set()

        while n != 1 and n not in visited:
            visited.add(n)
            n = count_total(n)
        if n == 1:
            return True
        else:
            return False 