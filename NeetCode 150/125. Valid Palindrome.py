class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_point = 0
        right_point = len(s) - 1

        while left_point < right_point:
            while not s[left_point].isalnum() and left_point < right_point:
                left_point = left_point + 1
            
            while not s[right_point].isalnum() and left_point < right_point:
                right_point = right_point - 1
            
            if s[left_point].lower() != s[right_point].lower():
                return False
            
            left_point = left_point + 1
            right_point = right_point - 1
        
        return True
            
            

