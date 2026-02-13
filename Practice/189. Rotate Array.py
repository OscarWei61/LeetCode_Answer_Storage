class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k = k % n
        
        def reverse_list(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]

                left = left + 1
                right = right - 1
        
        reverse_list(0, n - 1)
        reverse_list(0, k - 1)
        reverse_list(k, n - 1)