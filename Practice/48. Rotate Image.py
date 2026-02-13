class Solution(object):
    def rotate(self, matrix):
        N = len(matrix)
        if N == 0:
            return

        left, right = 0, N - 1
        top, bottom = 0, N - 1

        while left < right:
            
            for i in range(left, right):
                
                offset = i - left

                top_left_val = matrix[top][i]           

                matrix[top][i] = matrix[bottom - offset][left]            

                matrix[bottom - offset][left] = matrix[bottom][right - offset]           

                matrix[bottom][right - offset] = matrix[i][right]
                
                matrix[i][right] = top_left_val

            left += 1
            right -= 1
            top += 1
            bottom -= 1
            