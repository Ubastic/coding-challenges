# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def visit(node: 'TreeNode'):
            if node:
                left = visit(node.left)
                right = visit(node.right)

                if not left and node.val in (p.val, q.val):
                    left = node

                if not right and node.val in (p.val, q.val):
                    right = root

                if left and right:
                    return node
                else:
                    return left or right

        return visit(root)