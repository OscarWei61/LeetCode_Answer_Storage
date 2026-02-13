class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        match_num = 0
        s_index = 0

        for t_index in range(len(t)):
            if s_index < len(s):
                if t[t_index] == s[s_index]:
                    s_index = s_index + 1

        if s_index == len(s):
            return True
        else:
            return False
