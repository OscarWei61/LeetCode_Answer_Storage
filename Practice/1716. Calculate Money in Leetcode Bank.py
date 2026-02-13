class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        day_count = 1
        current_num = 1
        total = 0

        for day_count in range(1, n + 1):
            if day_count % 7 == 1 and day_count > 1:
                current_num = current_num - 7 + 1
            
            total = total + current_num
            current_num = current_num + 1
        
        return total
            