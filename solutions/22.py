class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def parens(pattern, open, remaining):
            if remaining == 0:
                res.append(pattern)
                return

            if remaining - open > 0:
                pattern = pattern + '('
                parens(pattern, open + 1, remaining - 1)
                pattern = pattern[:-1]
            if open > 0:
                pattern = pattern + ')'
                parens(pattern, open - 1, remaining - 1)
                pattern = pattern[:-1]

        parens('', 0, 2*n)
        return res
