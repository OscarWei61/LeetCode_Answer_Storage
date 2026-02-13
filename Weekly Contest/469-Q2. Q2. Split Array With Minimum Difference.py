class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        lowest_result = float('inf')

        # 前綴遞增
        increase_order = [False] * n
        increase_order[0] = True
        for i in range(1, n):
            if nums[i-1] < nums[i] and increase_order[i-1]:
                increase_order[i] = True

        # 後綴遞減
        decrease_order = [False] * n
        decrease_order[n-1] = True
        for i in range(n-2, -1, -1):
            if nums[i] > nums[i+1] and decrease_order[i+1]:
                decrease_order[i] = True

        # 前綴和
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        # 嘗試所有切點
        for i in range(1, n):
            if increase_order[i-1] and decrease_order[i]:
                first_sum = prefix_sum[i]
                second_sum = prefix_sum[n] - prefix_sum[i]
                lowest_result = min(lowest_result, abs(first_sum - second_sum))

        return lowest_result if lowest_result != float('inf') else -1