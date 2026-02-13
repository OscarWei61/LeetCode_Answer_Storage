class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        left_index = 0
        right_index = len(s) - 1
        count = 0

        while left_index <= right_index:
            if s[right_index] == " ":
                right_index = right_index - 1
            else:
                break

        while left_index <= right_index:
            if s[left_index] == " ":
                count = 0
            else:
                count = count + 1

            left_index = left_index + 1
            
        return count