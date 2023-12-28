class Solution:
    def trailingZeroes(self, n: int) -> int:
        out = 0

        while n > 0:
            n = n // 5
            out += n

        return out