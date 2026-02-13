class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        answer = [0] * (n + 1)

        for index in range(1, n + 1):
            answer[index] = answer[index >> 1] + (index & 1)
        
        return answer