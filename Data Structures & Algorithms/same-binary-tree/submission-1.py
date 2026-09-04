# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans = True

        def dfs(p, q):
            nonlocal ans

            if not p and not q:
                return

            if not p or not q:
                ans = False
                return

            dfs(p.left, q.left)
            dfs(p.right, q.right)
            if p.val != q.val: ans = False

        dfs(p, q)
        return ans

            
