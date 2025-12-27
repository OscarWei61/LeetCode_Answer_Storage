class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        
        points.sort(key=lambda x: x[1])

        arrows = 1
        current_arrow_pos = points[0][1]

        for point in points[1:]:
            if  current_arrow_pos < point[0]:
                current_arrow_pos = point[1]
                arrows = arrows + 1
        return arrows