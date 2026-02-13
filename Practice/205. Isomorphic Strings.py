class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_map = {}
        t_map = {}

        for c_index in range(len(s)):
            char_s = s[c_index]
            char_t = t[c_index]

            if char_s in s_map:
                if s_map[char_s] != char_t:
                    return False
            elif char_t in t_map:
                return False
            
            else:
                s_map[char_s] = char_t
                t_map[char_t] = char_s 
        
        return True