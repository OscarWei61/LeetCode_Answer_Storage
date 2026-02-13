class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        if not intervals:
            return 0

        intervals.sort(key = lambda x: x[1])

        count = 0
        end = float('-inf')

        for start, finish_point in intervals:
            if start < end:
                count = count + 1
            else:
                end = finish_point
        
        return count