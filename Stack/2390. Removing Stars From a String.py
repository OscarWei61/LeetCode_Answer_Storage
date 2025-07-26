class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        result = []
        
        for c in s_list:

            if c != '*':
                result.append(c)
                
            else:
                result.pop()

        return "".join(result)