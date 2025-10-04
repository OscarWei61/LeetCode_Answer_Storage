# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left_index = 1
        right_index = n

        while left_index <= right_index: 

            mid_index = (left_index + right_index) // 2
            result = guess(mid_index)

            if result == -1:
                right_index = mid_index - 1

            if result == 1:
                left_index = mid_index + 1
            
            if result == 0:
                return mid_index

        return -1