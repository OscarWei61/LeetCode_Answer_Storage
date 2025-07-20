class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        feasible_space = 0

        if len(flowerbed) == 1:
            return (flowerbed[0] == 0 and n <= 1) or (flowerbed[0] == 1 and n == 0)

                    

        for index in range(0, len(flowerbed)):
            if index == 0 and (index + 1) != len(flowerbed):
                if flowerbed[index] == 0 and flowerbed[index + 1] == 0:
                    flowerbed[index] = 1
                    feasible_space = feasible_space + 1
            
            if index != 0 and (index + 1) != len(flowerbed):
                if flowerbed[index - 1] == 0 and flowerbed[index] == 0 and flowerbed[index + 1] == 0:
                    flowerbed[index] = 1
                    feasible_space = feasible_space + 1
            
            if index != 0 and (index + 1) == len(flowerbed):
                if flowerbed[index - 1] == 0 and flowerbed[index] == 0:
                    flowerbed[index] = 1
                    feasible_space = feasible_space + 1
        
        if feasible_space >= n:
            return True
        else:
            return False