# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def visit(node: TreeNode, depth: int = 0):
            if not node:
                return depth

            return max(visit(node.left, depth + 1), visit(node.right ,depth + 1))
        
        return visit(root)