class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        # Better Solution
        cal_list = [1] * n

        for index_m in range(1, m):
            for index_n in range(1, n):
                cal_list[index_n] = cal_list[index_n] + cal_list[index_n - 1]

        return cal_list[n - 1]



        '''        
        if m == 1 or n == 1:
            return 1

        cal_list = [[0] * n for _ in range(0,m)]
        
        for index in range(1, n):
            cal_list[0][index] = 1

        for index in range(1, m):
            cal_list[index][0] = 1

        for index_m in range(1, m):
            for index_n in range(1, n):
                cal_list[index_m][index_n] = cal_list[index_m][index_n] + cal_list[index_m][index_n - 1] + cal_list[index_m - 1][index_n]    

        return cal_list[m - 1][n - 1]
        '''
s = Solution()
s.uniquePaths(3,7)