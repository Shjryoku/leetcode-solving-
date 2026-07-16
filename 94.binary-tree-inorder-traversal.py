#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.solver(root, result)
        return result

    def solver(self, root: TreeNode, result: List[int]) -> List[int]:
        if root is not None:
            self.solver(root.left, result)
            result.append(root.val)
            self.solver(root.right, result)
        
# @lc code=end

