class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        s_map = Counter(s)
        t_map = Counter(t)

        for c in s:
            if s_map[c] != t_map[c]:
                return False
        
        return True