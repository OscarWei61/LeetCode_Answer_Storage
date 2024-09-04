class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 0 or not s:
            return 0 

        if s[0] == '0':
            return 0 

        cal_list = [0] * (len(s) + 1)
        cal_list[0] = 1

        for index in range(1, len(s) + 1):
            if s[index - 1] != '0':
                cal_list[index] = cal_list[index] + cal_list[index - 1]
            
            if index > 1 and ('10' <= s[index-2:index] <= '26'):
                cal_list[index] = cal_list[index] + cal_list[index - 2]

        return cal_list[len(s)]