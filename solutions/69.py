class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 2:
            return 1
        for i in range(0, x):
            if i * i > x:
                return i - 1

        return x