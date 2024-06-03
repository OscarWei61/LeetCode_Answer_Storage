class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        index_m = m-1
        index_n = n-1
        index_mergeed = m+n-1
        while index_m >= 0 and index_n >= 0:
            if nums1[index_m] > nums2[index_n]:
                nums1[index_mergeed] = nums1[index_m]
                index_m = index_m - 1
                index_mergeed = index_mergeed - 1
            else:
                nums1[index_mergeed] = nums2[index_n]
                index_n = index_n - 1
                index_mergeed = index_mergeed - 1
        while index_n >= 0:
            nums1[index_mergeed] = nums2[index_n]
            index_n = index_n - 1
            index_mergeed = index_mergeed - 1