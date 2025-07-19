class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowel = set('aeiou')

        max_number = 0
        current_number = 0

        for index in range(0, k):
            if s[index] in vowel:
                current_number = current_number + 1
        max_number = current_number    
        for index in range(k, len(s)):
            if s[index - k] in vowel:
                current_number = current_number - 1
            
            if s[index] in vowel:
                current_number = current_number + 1
            
            max_number = max(max_number, current_number)

        return max_number