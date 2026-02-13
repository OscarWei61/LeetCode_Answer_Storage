class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        h = 0

        for index, c in enumerate(citations):
            if c >= index + 1:
                h = index + 1
            else:
                break
        
        return h