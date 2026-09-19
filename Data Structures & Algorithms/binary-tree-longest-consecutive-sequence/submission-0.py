# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        ans = 1
        def dfs(node: TreeNode | None, length: int, prev_val: int) -> int:
            nonlocal ans
            if not node:
                return
            if prev_val and node.val == prev_val + 1:
                length += 1
                ans = max(ans, length)
            else:
                length = 1
            
            dfs(node.left, length, node.val)
            dfs(node.right, length, node.val)


        dfs(root, 1, None)
        return ans

