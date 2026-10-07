class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0

        while n > 0:
            if n % 2 == 1:
                result = result * x

            x = x * x
            n = n // 2

        return result
    
    
print(Solution().myPow(2.00000, 10))  # Output: 1024.0