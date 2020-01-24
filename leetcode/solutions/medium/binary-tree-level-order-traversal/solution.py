# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = [root]
        res = []

        while queue:
            new_queue = []
            level = []

            for node in queue:
                level.append(node.val)

                if node.left:
                    new_queue.append(node.left)

                if node.right:
                    new_queue.append(node.right)

            queue = new_queue
            res.append(level)

        return res