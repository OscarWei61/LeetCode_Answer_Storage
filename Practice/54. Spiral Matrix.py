class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        result = []
        rows = len(matrix)
        cols = len(matrix[0])

        top, bottom = 0, rows - 1
        left, right = 0, cols - 1

        while top <= bottom and left <= right:
            

            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1  
            

            if top <= bottom: 
                for r in range(top, bottom + 1):
                    result.append(matrix[r][right])
                right -= 1 
            

            if top <= bottom and left <= right: 

                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1 
                

            if top <= bottom and left <= right: 
               
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])
                left += 1
                
        return result