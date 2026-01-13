class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x <0 else 1
        value = abs(x)

        result = 0

        while value > 0:
            last_digit = value % 10
            value = value // 10
            result = (result*10) + last_digit
        
        result = result * sign

        low = -2**31
        high = 2**31 -1

        if result < low or result > high:
            return 0

        return result

        