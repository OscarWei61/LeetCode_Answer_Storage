class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        current_string = set()
        left_point = 0
        current_string.add(s[left_point])
        max_length = 1
    
        for right_index in range(1, len(s)):
            if s[right_index] in current_string:
                while s[right_index] in current_string and left_point< right_index:
                    current_string.remove(s[left_point])
                    left_point = left_point + 1
            current_string.add(s[right_index])    
            max_length = max(max_length, len(current_string))
            
        return max_length