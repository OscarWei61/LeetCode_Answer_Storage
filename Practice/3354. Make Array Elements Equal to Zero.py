class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def find(nums, start_index, direction):
            arr = nums[:]
            n = len(nums)
            current_index = start_index

            while 0 <= current_index < n:
                if arr[current_index] == 0:
                    current_index = current_index + direction
                else:
                    arr[current_index] = arr[current_index] - 1
                    direction = direction * (-1)
                    current_index = current_index + direction
            
            if all(x == 0 for x in arr):
                return True
            else:
                return False
            
        res = 0
        for index in range(len(nums)):
            if nums[index] == 0:
                if find(nums, index, 1):
                    res = res + 1
                if find(nums, index, -1):  
                    res = res + 1
        
        return res