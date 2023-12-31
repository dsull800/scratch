class Solution:
    def __init__(self):
        self.memo = {}

    def wordBreak(self, s: str, wordDict: List[str], index=0) -> bool:
        if index == len(s):
            return True

        for i in range(index, len(s) + 1):
            if s[index:i] in wordDict and s[index:i] not in self.memo.get(i, set()):
                self.memo[i] = self.memo.get(i, set()).union(set([s[index:i]]))
                ret_val = self.wordBreak(s=s, wordDict=wordDict, index=i)
                if ret_val:
                    return ret_val
        return False