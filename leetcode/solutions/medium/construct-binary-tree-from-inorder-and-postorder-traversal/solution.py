# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        pre_index = len(inorder) - 1

        def visit(start, end):
            nonlocal pre_index

            if start > end:
                return None

            node = TreeNode(postorder[pre_index])
            pre_index -= 1

            if start == end:
                return node

            root = start + inorder[start: end + 1].index(node.val)

            node.right = visit(root + 1, end)
            node.left = visit(start, root - 1)

            return node

        return visit(0, len(inorder) - 1)