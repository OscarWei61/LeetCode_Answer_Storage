class Solution(object):
    def minTime(self, skill, mana):
        """
        :type skill: List[int]
        :type mana: List[int]
        :rtype: int
        """
        n, m = len(skill), len(mana)

        if n == 0 or m == 0:
            return 0

        prefix = [0] * n
        prefix[0] = skill[0] * mana[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + skill[i] * mana[0]

        
        gaps = []

        for j in range(0, m-1):
            
            nxt = [0] * n
            nxt[0] = skill[0] * mana[j+1]
            for i in range(1, n):
                nxt[i] = nxt[i-1] + skill[i] * mana[j+1]
            totals.append(nxt[-1])
            maxgap = prefix[0]
            for i in range(1, n):
                val = prefix[i] - nxt[i-1]
                if val > maxgap:
                    maxgap = val
            gaps.append(maxgap)
            prefix = nxt
        
        S = 0
        ans = 0

        ans = max(ans, S + totals[0])

        for j in range(1, m):
            S += gaps[j-1]
            cur_completion = S + totals[j]
            if cur_completion > ans:
                ans = cur_completion
        return ans
