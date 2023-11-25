class Solution:
    def minWindow(self, s: str, t: str) -> str:
        substr = ""
        len_best = 10 ** 6
        best_substr = ""
        chars_in_t = list(t)
        set_of_t = set(chars_in_t)
        order_t_found = []
        index_t_found = []
        freq_in_t = {}
        for ch in t:
            freq_in_t[ch] = freq_in_t.get(ch, 0) + 1

        for index, ch in enumerate(s):
            # substr = substr + ch
            if ch in set_of_t:
                freq_in_t[ch] = freq_in_t[ch] - 1
                order_t_found.append(ch)
                index_t_found.append(index)
                while not any(i > 0 for i in freq_in_t.values()):
                    first_found = order_t_found.pop(0)
                    index_found = index_t_found.pop(0)
                    freq_in_t[first_found] += 1
                    substr = s[index_found:index + 1]
                    if len(substr) < len_best:
                        len_best = len(substr)
                        best_substr = substr

        return best_substr