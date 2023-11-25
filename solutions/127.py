class Solution:
    def __init__(self):
        self.word_adjacencies = {}

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        def string_compare(string1, string2):
            count = 0
            for s_ind, (s_1, s_2) in enumerate(zip(string1, string2)):
                if s_1 != s_2:
                    count += 1
                    if count > 1:
                        return False
            return True

        if endWord not in wordList:
            return 0
        all_words = list(set([beginWord] + wordList))
        for word_ind, word1 in enumerate(all_words[:-1]):
            for word2 in all_words[word_ind + 1:]:
                if string_compare(word1, word2):
                    self.word_adjacencies[word1] = self.word_adjacencies.get(word1, []) + [word2]
                    self.word_adjacencies[word2] = self.word_adjacencies.get(word2, []) + [word1]

        # print(self.word_adjacencies)
        if len(self.word_adjacencies) == 0 or self.word_adjacencies.get(beginWord,
                                                                        None) is None or self.word_adjacencies.get(
                endWord, None) is None:
            return 0
        visited = set()
        frontier = deque(self.word_adjacencies[beginWord])
        frontier.appendleft(None)
        moves = 1

        while frontier:
            current_word = frontier.pop()
            if current_word is None:
                moves += 1
                if frontier:
                    frontier.appendleft(None)
                continue

            if current_word == endWord:
                return moves + 1

            frontier.extendleft([word for word in self.word_adjacencies[current_word] if word not in visited])
            visited = visited.union(self.word_adjacencies[current_word])

        return 0
