class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
<<<<<<< HEAD
        
        points.sort(key=lambda x: x[1])

        arrows = 1
        current_arrow_pos = points[0][1]

        for point in points[1:]:
            if  current_arrow_pos < point[0]:
                current_arrow_pos = point[1]
                arrows = arrows + 1
        return arrows
=======

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
>>>>>>> 3e7db307e40da2fcab20bde57f05f71dba334446
