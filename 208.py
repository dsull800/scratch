class Trie:
    class Node:
        def __init__(self, val=None, children=[], ending=False):
            self.val = val
            self.children = children
            self.ending = False

    def __init__(self):
        self.root = self.Node(None, [], False)

    def insert(self, word: str) -> None:
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

    def search(self, word: str) -> bool:
        root = self.root
        for letter in word:
            found = False
            for child in root.children:
                if child.val == letter:
                    root = child
                    found = True
                    break

            if not found:
                return False

        return root.ending

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for letter in prefix:
            found = False
            for child in root.children:
                if child.val == letter:
                    root = child
                    found = True
                    break

            if not found:
                return False

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)