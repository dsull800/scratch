class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        memo = [False] * (amount + 1)  # {amount - coin: 1 for coin in coins}
        for coin in coins:
            if 0 <= amount - coin < len(memo):
                memo[amount - coin] = 1

        for i in range(amount - min(coins), -1, -1):
            for coin in coins:
                if i + coin < len(memo) and memo[i + coin]:
                    memo[i] = min(1 + memo[i + coin], memo[i] if memo[i] else float('inf'))

        return memo[0] if memo[0] else -1