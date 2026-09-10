# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans = float("inf")
        def dfs(node, target):
            nonlocal ans
            if not node:
                return
            if abs(node.val - target) < abs(ans-target):
                ans = node.val
            if target <= node.val:
                dfs(node.left, target)
            else:
                dfs(node.right, target)

        dfs(root, target)
        return ans
    
            