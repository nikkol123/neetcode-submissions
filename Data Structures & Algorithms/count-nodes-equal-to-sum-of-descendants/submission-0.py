# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def equalToDescendants(self, root: TreeNode) -> int:
        
        total = 0

        def dfs(node):
            nonlocal total
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left + right == node.val:
                total += 1
            
            return left + right + node.val
        
        dfs(root)
        return total
            