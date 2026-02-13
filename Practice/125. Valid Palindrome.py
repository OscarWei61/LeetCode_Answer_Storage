class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_point = 0
        right_point = len(s) - 1

        while left_point <= right_point:
            
            while left_point < right_point and not s[left_point].isalnum():
                left_point = left_point + 1
            
            while left_point < right_point and not s[right_point].isalnum():
                right_point = right_point - 1
            
            if s[left_point].lower() != s[right_point].lower():
                return False
            
            left_point = left_point + 1
            right_point = right_point - 1
        
        return True