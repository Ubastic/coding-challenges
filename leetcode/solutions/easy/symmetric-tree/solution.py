# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def visit(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right:
                return True
            
            if left and right and left.val == right.val:
                return visit(left.left, right.right) and visit(right.left, left.right)
            
            return False
        
        return visit(root, root)