class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        map_list = defaultdict(list)

        for a,b in connections:
            map_list[a].append((b, 1))
            map_list[b].append((a, 0))
            
        move = 0
        visited = [False] * n
        q = deque([0])
        visited[0] = True
        #print("map_list", map_list)
        #print("q", q)
        while q:
            next_node = q.popleft()

            for v, turn in map_list[next_node]:
                #print("q", q)
                if not visited[v]:
                    move = move + turn
                    visited[v] = True
                    q.append(v)
        return move