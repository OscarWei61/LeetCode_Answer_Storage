class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        prev_value = 0
        value_dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "N/A": 0}

        for symbol in reversed(s):
            current = value_dictionary[symbol]

            if current < prev_value:
                total -= current
            else:
                total += current
            
            prev_value = current
        
        return total