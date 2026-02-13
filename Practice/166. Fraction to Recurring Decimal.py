class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"

        result = []

        if (numerator < 0) ^ (denominator < 0):
            result.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        result.append(str(numerator // denominator))
        remainder = numerator % denominator

        if remainder == 0:
            return "".join(result)

        result.append(".")

        remainder_map = {}

        while remainder != 0:
            if remainder in remainder_map:
                idx = remainder_map[remainder]
                result.insert(idx, "(")
                result.append(")")
                break

            remainder_map[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(result)
