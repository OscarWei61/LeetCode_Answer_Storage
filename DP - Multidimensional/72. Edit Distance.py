class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        m = len(word1)
        n = len(word2)

        dp_list = [[0] * (n + 1) for _ in range(m + 1)]

        for index in range(m + 1):
            dp_list[index][0] = index
        
        for index in range(n + 1):
            dp_list[0][index] = index

        for index_m in range(1, m + 1):
            for index_n in range(1, n + 1):
                if word1[index_m - 1] == word2[index_n - 1]:
                    dp_list[index_m][index_n] = dp_list[index_m - 1][index_n - 1]
                else:
                    dp_list[index_m][index_n] = min(
                        dp_list[index_m - 1][index_n] + 1,
                        dp_list[index_m][index_n - 1] + 1,
                        dp_list[index_m - 1][index_n - 1] + 1
                    ) 
        
        return dp_list[-1][-1]