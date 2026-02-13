class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        
        n = len(nums)
        count = Counter(nums[:k])
        result = []

        def count_sum(counter):
            sorted_counter = sorted(counter.items(), key=lambda p: (-p[1], -p[0]))
            top_elements = {num for num, _ in sorted_counter[:x]}
            total = sum(num * counter[num] for num in top_elements)
            return total
        
        result.append(count_sum(count))

        for index in range(k, n):
            left_num = nums[index - k]
            right_num = nums[index]

            count[left_num] = count[left_num] - 1

            if count[left_num] == 0:
                del count[left_num]

            count[right_num] = count[right_num] + 1

            result.append(count_sum(count))
        
        return result