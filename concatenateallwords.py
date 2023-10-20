class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        current_index = 0
        sol = []

        def rec_func(sub_string, sub_words):
            sub_words_copy = copy.copy(sub_words)
            for word in sub_words:
                if sub_string[:len(word)] == word:
                    sub_words_copy.remove(word)
                    return rec_func(sub_string[len(word):], sub_words_copy)
                else:
                    pass
            if len(sub_words) == 0:
                return True

        while current_index < len(s) - len(words) * len(words[0]) + 1:
            res = rec_func(s[current_index:], words)
            if res:
                sol.append(current_index)
                current_index += 1
            else:
                current_index += 1
        return sol