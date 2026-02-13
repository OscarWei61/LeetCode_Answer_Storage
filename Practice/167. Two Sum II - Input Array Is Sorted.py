class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_index = 0
        right_index = len(numbers) - 1

        while left_index <= right_index:
            if numbers[left_index] + numbers[right_index] > target:
                right_index = right_index - 1

            elif numbers[left_index] + numbers[right_index] < target:
                left_index = left_index + 1
            
            else:
                return [left_index + 1, right_index + 1]