class SmallestInfiniteSet(object):

    def __init__(self):
        self.heap = []
        self.heap_set = set()
        self.current_num = 1

    def popSmallest(self):
        """
        :rtype: int
        """
        if self.heap:
            smallest_item = heapq.heappop(self.heap)
            self.heap_set.remove(smallest_item)
            return smallest_item
        else:
            self.current_num = self.current_num + 1
            return self.current_num - 1

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num < self.current_num and num not in self.heap_set:
            heapq.heappush(self.heap, num)
            self.heap_set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)