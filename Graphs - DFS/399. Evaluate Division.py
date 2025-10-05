class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
        graph = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val
        
        def dfs(start, end, visited):
            if start == end:
                return 1
            
            visited.add(start)

            for node, val in graph[start].items():
                if node in visited:
                    continue
                
                res = dfs(node, end, visited)
                if res != -1:
                    return val * res
            
            return -1
        
        results = []

        for c, d in queries:
            if c not in graph or d not in graph:
                results.append(-1)
            elif c == d:
                results.append(1)
            else:
                results.append(dfs(c, d, set()))
        
        return results
