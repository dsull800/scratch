class Solution:
    def reverseBits(self, n: int) -> int:
        num = bin(n)[2:]
        num = (32 - len(num)) * '0' + num
        return int(num[::-1], 2)