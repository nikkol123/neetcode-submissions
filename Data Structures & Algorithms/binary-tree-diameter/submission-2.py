# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0 

        def dfs(node):
            nonlocal res

            if not node:
                return 0
            left_child=dfs(node.left)
            right_child=dfs(node.right)

            res = max(res, left_child + right_child)
            return 1 + max(left_child, right_child)

        dfs(root)
        return res


