class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        left_index = 0
        right_index = len(s) - 1
        vowels_list = set('aeiouAEIOU')
        while left_index < right_index:
            while left_index < right_index and s[left_index] not in vowels_list:
                left_index = left_index + 1
            
            while left_index < right_index and s[right_index] not in vowels_list:
                right_index = right_index - 1
            
            s[right_index], s[left_index] = s[left_index], s[right_index]
            right_index = right_index - 1
            left_index = left_index + 1
        return "".join(s)