# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def set_relationships(nums):
            if not nums:
                return

            arr_split = ceil(len(nums)/2) - 1
            new_node = TreeNode(val=nums[arr_split])
            new_node.left = set_relationships(nums[:arr_split])
            new_node.right = set_relationships(nums[arr_split+1:])
            return new_node

        if not nums:
            return TreeNode()

        return set_relationships(nums)
