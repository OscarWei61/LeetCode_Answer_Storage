class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        # Step 1: Record rows and columns that need to be zeroed
        zero_rows = set()
        zero_cols = set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        # Step 2: Zero out the rows
        for row in zero_rows:
            for j in range(n):
                matrix[row][j] = 0
        
        # Step 3: Zero out the columns
        for col in zero_cols:
            for i in range(m):
                matrix[i][col] = 0