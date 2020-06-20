# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def visit(node: TreeNode, path: int = 0) -> bool:
            if not node:
                return False
            
            if not node.left and not node.right:
                return path + node.val == sum

            return visit(node.left, path + node.val) or visit(node.right, path + node.val)
        
        return visit(root)