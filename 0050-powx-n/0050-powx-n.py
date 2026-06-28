class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle negative exponents: x^(-n) = 1 / x^n
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0
        current_power = x

        while n > 0:
            if n % 2 == 1:
                result *= current_power
            current_power *= current_power
            n //= 2

        return result