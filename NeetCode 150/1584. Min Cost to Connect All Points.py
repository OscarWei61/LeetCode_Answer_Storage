class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        total_distance = 0
        mini_heap = []
        heapq.heappush(mini_heap, (0, 0))
        visited = set()

        while len(visited) < len(points):
            d, current_point_index = heapq.heappop(mini_heap)
            
            if current_point_index in visited:
                continue

            visited.add(current_point_index)
            total_distance = total_distance + d

            for p in range(len(points)):
                if p not in visited:
                    distance = abs(points[p][0] - points[current_point_index][0]) + abs(points[p][1] - points[current_point_index][1])
                    heapq.heappush(mini_heap, (distance, p))

        return total_distance