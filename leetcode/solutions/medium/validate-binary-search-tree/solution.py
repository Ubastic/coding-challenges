class Solution:
    def isValidBST(self, node: TreeNode, min=float('-inf'), max=float('inf')) -> bool:
        return not node or (
                min < node.val < max
                and self.isValidBST(node.left, min, node.val)
                and self.isValidBST(node.right, node.val, max)
        )


