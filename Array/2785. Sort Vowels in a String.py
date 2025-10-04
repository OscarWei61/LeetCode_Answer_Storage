class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels_list = 'aeiouAEIOU'
        v_list = []
        for c in s:
            if c in vowels_list:
                v_list.append(c)
        v_list.sort()
        s_list = list(s)
        
        point = 0
        for c in range(len(s_list)):
            if s_list[c] in vowels_list:
                s_list[c] = v_list[point]
                point = point + 1
            
        return ''.join(s_list)