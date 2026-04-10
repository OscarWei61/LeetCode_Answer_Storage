class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.score_list = nums
        self.k = k
        
        heapq.heapify(self.score_list)

        while len(self.score_list) > k:
            heapq.heappop(self.score_list)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """

        heapq.heappush(self.score_list, (val))

        if len(self.score_list) > self.k:
            heapq.heappop(self.score_list)
        

        return self.score_list[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)