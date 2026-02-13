class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        points.sort(key=lambda x: x[1])

        arrow_point = points[0][1]
        arrow_count = 1

        for p in points[1:]:
            if p[0] <= arrow_point:
                continue
            else:
                arrow_count = arrow_count + 1
                arrow_point = p[1]
        
        return arrow_count