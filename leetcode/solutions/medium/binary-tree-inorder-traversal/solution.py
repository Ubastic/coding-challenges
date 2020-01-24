# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def visit(node: TreeNode):
            if node:
                visit(node.left)
                res.append(node.val)
                visit(node.right)

        visit(root)
        return res