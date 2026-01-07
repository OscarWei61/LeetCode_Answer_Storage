class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = 0

        for n in nums:
            divisors = set()

            for index in range(1, int(math.sqrt(n)) + 1):
                if n % index == 0:
                    divisors.add(index)
                    divisors.add(n // index)
                
                if len(divisors) > 4:
                    break
                
            if len(divisors) == 4:
                total_sum = total_sum + sum(divisors)
        
        return total_sum