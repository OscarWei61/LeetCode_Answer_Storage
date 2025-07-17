class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_index = 0

        for c in t:
            if s_index < len(s) and c == s[s_index]:
                s_index = s_index + 1
            
        if s_index == len(s):
            return True
        
        return False