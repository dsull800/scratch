# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(postorder[-1])
        inorder_left_frontier = []
        for index, in_node in enumerate(inorder):
            if in_node != root.val:
                inorder_left_frontier.append(in_node)
            else:
                break
        inorder_right_frontier = inorder[index+1:]

        if inorder_left_frontier and postorder[:index]:
            root.left = self.buildTree(inorder_left_frontier, postorder[:index])
        if inorder_right_frontier and postorder[index:-1]:
            root.right = self.buildTree(inorder_right_frontier, postorder[index:-1])
        return root