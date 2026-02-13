class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        if n == 0:
            return nums1[:m]

        nums1_index = m - 1
        nums2_index = n - 1
        p = m + n - 1

        while nums1_index >= 0 and nums2_index >= 0:
            if nums1[nums1_index] >= nums2[nums2_index]:
                nums1[p] = nums1[nums1_index]
                nums1_index = nums1_index - 1
            else:
                nums1[p] = nums2[nums2_index]
                nums2_index = nums2_index - 1
            
            p = p - 1
        
        while nums2_index >= 0:
            
            nums1[p] = nums2[nums2_index]
            nums2_index = nums2_index - 1
            
            p = p - 1
        
        