# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        LCA = root
        first = min(p.val, q.val)
        second = max(p.val, q.val)
        def traverse(node):
            nonlocal LCA

            if first < node.val and node.val < second:
                LCA = node
                return

            if node.val == second or node.val == first:
                LCA = node
                return

            if second < node.val:
                return traverse(node.left)
            if first > node.val:
                return traverse(node.right)

        traverse(root)
        return LCA