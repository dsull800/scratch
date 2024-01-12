class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        depth = len(triangle)

        memo = {}

        for d in range(depth-1, -1, -1):
            for c in range(0, d+1):
                if d == depth - 1:
                    memo[(d,c)] = triangle[d][c]
                    continue
                memo[(d,c)] = min(
                                    triangle[d][c] + memo[(d+1,c)],
                                    triangle[d][c] + memo[(d+1,c+1)]
                                )
        return memo[(0, 0)]
