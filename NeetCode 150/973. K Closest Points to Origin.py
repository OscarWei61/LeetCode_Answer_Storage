class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        mini_heap = []
        result = []

        for p in points:
            d = p[0] ** 2 + p[1] ** 2

            heapq.heappush(mini_heap, (-d, p))
            if len(mini_heap) > k:
                heapq.heappop(mini_heap)
        
        while mini_heap:
            d, p =  heapq.heappop(mini_heap)
            result.append(p)
        
        return result