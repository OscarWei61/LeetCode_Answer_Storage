class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        heap_left = []
        heap_right = []
        
        total_cost = 0
        count = 1
            
        left_index = 0
        right_index = len(costs) - 1
  
        for count in range(candidates):
            if left_index <= right_index:
                heapq.heappush(heap_left, (costs[left_index], left_index))
                left_index = left_index + 1

            if left_index <= right_index:
                heapq.heappush(heap_right, (costs[right_index], right_index))
                right_index = right_index - 1

        for candidate_num in range(k):
            if heap_left and heap_right:
                if heap_left[0] <= heap_right[0]:
                    cost, _ = heapq.heappop(heap_left)
                    total_cost += cost
                    if left_index <= right_index:
                        heapq.heappush(heap_left, (costs[left_index], left_index))
                        left_index += 1
                else:
                    cost, _ = heapq.heappop(heap_right)
                    total_cost += cost
                    if left_index <= right_index:
                        heapq.heappush(heap_right, (costs[right_index], right_index))
                        right_index -= 1
            elif heap_left:
                cost, _ = heapq.heappop(heap_left)
                total_cost += cost
                if left_index <= right_index:
                    heapq.heappush(heap_left, (costs[left_index], left_index))
                    left_index += 1
            else:
                cost, _ = heapq.heappop(heap_right)
                total_cost += cost
                if left_index <= right_index:
                    heapq.heappush(heap_right, (costs[right_index], right_index))
                    right_index -= 1

        return total_cost
            