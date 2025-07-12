class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        len1 = len(word1)
        len2 = len(word2)
        w_index1 = 0
        w_index2 = 0

        while w_index1 < len1 or w_index2 < len2:
            if w_index1 < len1:
                result.append(word1[w_index1])
                w_index1 = w_index1 + 1
            if w_index2 < len2:
                result.append(word2[w_index2])  
                w_index2 = w_index2 + 1

        return "".join(result)