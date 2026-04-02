class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        mini_heap = []
        for stone in stones:
            heapq.heappush(mini_heap, stone * (-1))

        while len(mini_heap) > 1:

            largest1 = heapq.heappop(mini_heap) * (-1)
            largest2 = heapq.heappop(mini_heap) * (-1)
            heapq.heappush(mini_heap, (-1) * (largest1 - largest2))

        if len(mini_heap) == 0:
            return 0
        else:
            return mini_heap[0] * -1