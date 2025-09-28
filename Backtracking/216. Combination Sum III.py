class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        result = []

        def backtrack(start, path, total):
            if len(path) == k:
                if total == n:
                    result.append(path[:])
                
                return
            
            for index in range(start, 10):
                if total + index > n:
                    break
                
                path.append(index)
                backtrack(index + 1, path, total + index)
                path.pop()
        
        backtrack(1, [], 0)
        return result