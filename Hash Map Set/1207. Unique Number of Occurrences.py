from collections import Counter
        
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        count = Counter(arr)
        freq = list(count.values())

        if len(freq) == len(set(freq)):
            return True
        else:
            return False
