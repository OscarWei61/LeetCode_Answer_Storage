class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        sort_pairs = sorted(zip(nums2, nums1), reverse=True)
        heap = []
        heap_sum = 0
        result = 0

        for n2, n1 in sort_pairs:
            heapq.heappush(heap, n1)
            heap_sum = heap_sum + n1

            if len(heap) > k:
                heap_sum = heap_sum - heapq.heappop(heap)
 
            if len(heap) == k:
                result = max(result, heap_sum * n2)

        return result