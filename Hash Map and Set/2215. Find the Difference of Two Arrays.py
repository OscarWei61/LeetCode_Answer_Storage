class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        list1 = []
        list2 = []

        nums1_set = set(nums1)
        nums2_set = set(nums2)

        return [list(nums1_set - nums2_set), list(nums2_set - nums1_set)]