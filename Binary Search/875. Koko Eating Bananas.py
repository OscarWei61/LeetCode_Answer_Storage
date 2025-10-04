class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left_index = 1
        right_index = max(piles)

        while left_index < right_index:
            mid_index = (left_index + right_index) // 2
            time = 0
            for p in piles:
                if p % mid_index == 0:
                    time = time + p / mid_index
                else:
                    time = time + p // mid_index + 1
            
            if time > h:
                left_index = mid_index + 1
            else:
                right_index = mid_index
            
        return left_index
