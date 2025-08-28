class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        current_string = []
        num_prev = []
        string_prev = []
        num = 0

        for index in range(0, len(s)):
            if s[index].isdigit():
                num = num * 10 + int(s[index])
            
            elif s[index] == '[':
                num_prev.append(num)
                string_prev.append(''.join(current_string))
                current_string = []
                num = 0

            elif s[index]  == ']':
                prev_string = string_prev.pop()
                current_string = [''.join(prev_string) + ''.join(current_string) * num_prev.pop()]
            else:
                current_string.append(s[index])
            
        return ''.join(current_string)
            
