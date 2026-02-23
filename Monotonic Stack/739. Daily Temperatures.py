class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        num = len(temperatures)
        answer = [0] * num
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temperatures[index] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                answer[prev_day] = index - prev_day
            stack.append(index)

        return answer