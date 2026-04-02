class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0

        left_pointer = 0
        right_pointer = len(height) - 1

        while left_pointer < right_pointer:
            area = (right_pointer - left_pointer) * min(height[left_pointer], height[right_pointer])
            max_area = max(max_area, area)

            if height[left_pointer] < height[right_pointer]:
                left_pointer = left_pointer + 1
            else:
                right_pointer = right_pointer - 1

        return max_area