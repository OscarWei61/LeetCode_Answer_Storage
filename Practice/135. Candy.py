class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candy = [1] * len(ratings)

        for index in range(len(ratings) - 1):
            if ratings[index + 1] > ratings[index]:
                if candy[index + 1] == max(candy[index + 1], candy[index]) and candy[index + 1] != candy[index]:
                    continue
                else:
                    candy[index + 1] = max(candy[index + 1], candy[index]) + 1
            
        for index in range(len(ratings) - 1, 0, -1):
            if ratings[index - 1] > ratings[index]:
                if candy[index - 1] == max(candy[index - 1], candy[index]) and candy[index - 1] != candy[index]:
                    continue
                else:
                    candy[index - 1] = max(candy[index - 1], candy[index]) + 1
        
        return sum(candy)
         