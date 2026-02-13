class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = "aeiouAEIOU"
        num = 0

        for c in s:
            if c in vowels:
                num = num + 1
            
        if num > 0:
            return True
        else:
            return False