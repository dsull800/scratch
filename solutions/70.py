class Solution:
    def __init__(self):
        self.memo = {}

    def climbStairs(self, n: int) -> int:
        def recurse(n):
            if n == 0:
                return 0
            elif n < 0:
                return -1
            elif self.memo.get(n, None):
                return self.memo[n]
            self.memo[n] = 1 + recurse(n-1) + recurse(n-2)

            return self.memo[n]

        recurse(n)
        return self.memo[n] + 1
