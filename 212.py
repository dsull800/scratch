######################### FIRST pass, took to long and couldn't pass testcases
class Solution:
    class Node:
        def __init__(self, val=None, children={}, ending=False, final_word=None):
            self.val = val
            self.children = children
            self.ending = ending
            self.final_word = None

    def __init__(self):
        self.root = self.Node(val=None, children={}, ending=False)

    def search_word(self, word):
        root = self.root
        for letter in word:
            children = root.children.get(letter, None)
            if children is None:
                return False
            root = children
        return root.ending

    def get_next(self, letter, root):
        return root.children.get(letter, None)

    def insert_word(self, word):
        root = self.root
        for letter in word:
            children = root.children.get(letter, None)
            if children is None:
                children = self.Node(val=letter, children={}, ending=False)
                root.children[letter] = children

            root = children
        root.ending = True
        root.final_word = word

    def dfs(self, row, column, visited, root):
        output = []
        if (row, column) in visited:
            return []
        elif root is None:
            return []
        else:
            visited = visited.union(set([(row, column)]))

        if root.ending:
            output.extend([root.final_word])

        if len(root.children) == 0:
            return output

        root = self.get_next(self.board[row][column], root)
        if root is None:
            return output

        if root.ending:
            output.extend([root.final_word])

        if row + 1 < self.m:
            out = self.dfs(row + 1, column, visited, root)
            output.extend(out)

        if row - 1 >= 0:
            out = self.dfs(row - 1, column, visited, root)
            output.extend(out)

        if column + 1 < self.n:
            out = self.dfs(row, column + 1, visited, root)
            output.extend(out)

        if column - 1 >= 0:
            out = self.dfs(row, column - 1, visited, root)
            output.extend(out)

        return output

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        for word in words:
            self.insert_word(word)

        self.m = len(board)
        self.n = len(board[0])

        total_out = []

        for row in range(0, self.m):
            for column in range(0, self.n):
                root = self.root
                visited = set()
                out = self.dfs(row, column, visited, root)
                total_out.extend(out)

        return list(set(total_out))

################# Second Pass after looking at solutions, it works
class Solution:
    class Node:
        def __init__(self, val=None, children={}, ending=False, final_word=None):
            self.val = val
            self.children = children
            self.ending = ending
            self.final_word = None

    def __init__(self):
        self.root = self.Node(val=None, children={}, ending=False)

    def search_word(self, word):
        root = self.root
        for letter in word:
            children = root.children.get(letter, None)
            if children is None:
                return False
            root = children
        return root.ending

    def get_next(self, letter, root):
        return root.children.get(letter, None)

    def insert_word(self, word):
        root = self.root
        for letter in word:
            children = root.children.get(letter, None)
            if children is None:
                children = self.Node(val=letter, children={}, ending=False)
                root.children[letter] = children

            root = children
        root.ending = True
        root.final_word = word

    def dfs(self, row, column, root):
        if self.board[row][column] == '#':
            return []
        output = []

        if root.ending:
            output.extend([root.final_word])
            if len(root.children) == 0:
                del root
                return output

        root = self.get_next(self.board[row][column], root)
        if root is None:
            return output

        if root.ending:
            output.extend([root.final_word])
            if len(root.children) == 0:
                del root
                return output

        tmp = self.board[row][column]
        self.board[row][column] = '#'
        if row + 1 < self.m:
            out = self.dfs(row + 1, column, root)
            output.extend(out)

        if row - 1 >= 0:
            out = self.dfs(row - 1, column, root)
            output.extend(out)

        if column + 1 < self.n:
            out = self.dfs(row, column + 1, root)
            output.extend(out)

        if column - 1 >= 0:
            out = self.dfs(row, column - 1, root)
            output.extend(out)
        self.board[row][column] = tmp
        return output

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        for word in words:
            self.insert_word(word)

        self.m = len(board)
        self.n = len(board[0])

        total_out = []

        for row in range(0, self.m):
            for column in range(0, self.n):
                root = self.root
                out = self.dfs(row, column, root)
                total_out.extend(out)

        return list(set(total_out))