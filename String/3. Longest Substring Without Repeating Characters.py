class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left_index = 0
        right_index = 0
        char_dict = {}
        max_length = 0

        for right_index in range(len(s)):
            if s[right_index] in char_dict and char_dict[s[right_index]] >= left_index:
                left_index = char_dict[s[right_index]] + 1
            
            char_dict[s[right_index]] = right_index

            max_length = max(max_length, right_index - left_index + 1)

        return max_length