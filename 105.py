# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        inorder_left_frontier = []
        for index, in_node in enumerate(inorder):
            if in_node != root.val:
                inorder_left_frontier.append(in_node)
            else:
                break
        inorder_right_frontier = inorder[index+1:]

        if inorder_left_frontier and preorder[1:]:
            root.left = self.buildTree(preorder[1:], inorder_left_frontier)
        if inorder_right_frontier and preorder[index+1:]:
            root.right = self.buildTree(preorder[index+1:], inorder_right_frontier)
        return root



