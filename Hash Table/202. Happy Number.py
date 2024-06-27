class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n == 1:
            return True

        seen = set() 
               
        while n!= 1:
            seen.add(n)
            n = sum(int(i)**2 for i in str(n))
            if n == 1:
                return True
            if n in seen:
                return False

