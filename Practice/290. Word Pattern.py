class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        

        s = s.split(' ')
        if len(s) != len(pattern):
            return False
        
        pattern_map = {}
        s_map = {}

        for index in range(len(pattern)):
            if pattern[index] not in pattern_map:
                pattern_map[pattern[index]] = s[index]
            else:
                if pattern_map[pattern[index]] != s[index]:
                    return False
            if s[index] not in s_map:
                s_map[s[index]] = pattern[index]
            else:
                if s_map[s[index]] != pattern[index]:
                    return False
        return True
