class Solution:
    def hammingWeight(self, n: int) -> int:
        num = bin(n)[2:].count('1')
        return num