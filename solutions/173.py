# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def inorder(self, node):
        if node:
            yield from self.inorder(node.left)
            yield node.val
            yield from self.inorder(node.right)

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.generator = self.inorder(root)
        self.has_next_called = False
        self.next_node = None

    def next(self) -> int:
        value = next(self.generator) if not self.has_next_called else self.next_node
        self.has_next_called = False
        self.next_node = None
        return value

    def hasNext(self) -> bool:
        if not self.has_next_called:
            try:
                self.next_node = next(self.generator)
                self.has_next_called = True
                return True
            except Exception as e:
                print(e)
                return False
        else:
            return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()