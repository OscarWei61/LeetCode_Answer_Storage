class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Better solution
        element_nums1 = set(nums1)
        result = set()
        
        for item in nums2:
            if item in element_nums1:
                result.add(item)
                
        return list(result)
        
        # Worse solution
        '''
        element_nums1 = []
        result = []
        for item in nums1:
            if item not in element_nums1:
                element_nums1.append(item)
        for item in nums2:
            if item in element_nums1 and (item not in result):
                result.append(item)
        return result
        '''
        
'''
Time Complexity:

Method 1 (Using Lists):

Building element_nums1: O(n) where n is the length of nums1.
Checking membership in element_nums1: O(n) for each check.
Building the result list: O(m) where m is the length of nums2.
Checking membership in result: O(m) for each check.
Overall time complexity: O(n^2 + m^2).
Method 2 (Using Sets):

Building element_nums1: O(n) where n is the length of nums1.
Checking membership in element_nums1: O(1) on average for each check.
Building the result set: O(m) where m is the length of nums2.
Overall time complexity: O(n + m).
'''

solution = Solution()
print(solution.intersection([1,2,2,1], [2,2]))