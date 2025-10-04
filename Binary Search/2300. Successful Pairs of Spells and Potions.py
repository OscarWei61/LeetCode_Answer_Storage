class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        result = []
        potions.sort()

        for s in spells:
            
            left_index = 0
            right_index = len(potions) - 1
            
            while left_index <= right_index:
                mid_index = (left_index + right_index) // 2
                if potions[mid_index] * s >= success:
                    right_index = mid_index - 1
                elif potions[mid_index] * s < success:
                    left_index = mid_index + 1
                else:
                    break

            result.append(len(potions) - left_index)
        
        return result