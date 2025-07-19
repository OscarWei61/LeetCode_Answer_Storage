from collections import Counter

class Solution(object):
    def maxOperations(self, nums, k):
        counter = Counter(nums)

        operations = 0

        for num in list(counter.keys()):
            complement = k - num
            if complement in counter:
                if num == complement:
                    operations = operations + counter[num] // 2
                
                else:
                    pairs = min(counter[num], counter[complement])
                    
                    operations = operations + pairs

                    counter[num] = counter[num] - pairs
                    counter[complement] = counter[complement] - pairs
            
        return operations