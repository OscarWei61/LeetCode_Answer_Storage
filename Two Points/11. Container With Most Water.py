class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_index = 0
        right_index = len(height) - 1
        max_vloume = 0
        while left_index < right_index:

            max_vloume = max(min(height[left_index], height[right_index]) * (right_index - left_index), max_vloume)

            if height[left_index] < height[right_index]:
                left_index = left_index + 1
            else:
                right_index = right_index - 1
        
        return max_vloume