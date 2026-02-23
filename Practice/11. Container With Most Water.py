class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_index = 0
        right_index = len(height) - 1

        max_area = 0

        while left_index < right_index:

            max_area = max(max_area, (right_index - left_index) * min(height[left_index], height[right_index]))
            
            if height[left_index] < height[right_index]:
                left_index = left_index + 1
            else:
                right_index = right_index - 1
        
        return max_area