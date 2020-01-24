# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        pre_index = 0

        def visit(start, end):
            nonlocal pre_index

            if start > end:
                return None

            node = TreeNode(preorder[pre_index])
            pre_index += 1

            if start == end:
                return node

            root = start + inorder[start: end + 1].index(node.val)

            node.left = visit(start, root - 1)
            node.right = visit(root + 1, end)

            return node

        return visit(0, len(inorder) - 1)
