class WordDictionary:
    class Node:
        def __init__(self, val=None, children=[], ending=False):
            self.val = val
            self.children = children
            self.ending = ending

    def __init__(self):
        self.root = self.Node(val=None, children=[])

    def addWord(self, word: str) -> None:
        root = self.root
        for letter in word:
            found = False
            for child in root.children:
                if child.val == letter:
                    root = child
                    found = True
                    break

            if not found:
                new_node = self.Node(val=letter, children=[], ending=False)
                root.children.append(new_node)
                root = new_node

        root.ending = True

    def search(self, word: str, root=None) -> bool:
        if not root:
            root = self.root
        for idx, letter in enumerate(word):
            if letter == '.':
                for child in root.children:
                    outcome = self.search(word=word[idx + 1:], root=child)
                    if outcome:
                        return outcome
                return False
            else:
                found = False
                for child in root.children:
                    if child.val == letter:
                        root = child
                        found = True
                        break

                if not found:
                    return found

        return root.ending

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)