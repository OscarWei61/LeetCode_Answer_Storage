class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_number = max(candies)
        bool_result = []

        for index in range(len(candies)):
            if candies[index] + extraCandies >= max_number:
                bool_result.append(True)
            else:
                bool_result.append(False)
        
        return bool_result