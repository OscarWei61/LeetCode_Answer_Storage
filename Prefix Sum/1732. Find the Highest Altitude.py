class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        highest = 0
        altitudes = 0
        for g in gain:
            altitudes = altitudes + g
            highest = max(altitudes, highest)

        return highest