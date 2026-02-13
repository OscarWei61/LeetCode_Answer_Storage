class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        
        n = len(rains)

        ans = [-1] * n

        lake_next_rain = {}
        next_rain_index = {}

        days = defaultdict(list)

        for i, lake in enumerate(rains):
            if lake > 0:
                days[lake].append(i)
        
        heap = []
        full = set()

        for index, lake in enumerate(rains):
            if lake > 0:
                if lake in full:
                    return []
                
                full.add(lake)
                ans[index] = -1
            
                days[lake].pop(0)

                if days[lake]:
                    heapq.heappush(heap, (days[lake][0], lake))

            else:
                if heap:
                    next_day, dry_lake = heapq.heappop(heap)
                    full.remove(dry_lake)
                    ans[index] = dry_lake
                else:
                    ans[index] = 1

        return ans