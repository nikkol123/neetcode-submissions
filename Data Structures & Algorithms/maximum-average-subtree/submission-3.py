# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        maximumAverage = 0

        #state is a tuple (total, number of elements)
        def dfs(root):
            nonlocal maximumAverage
            if not root:
                return (0,0)

            counter = 1

            left = dfs(root.left)

            right = dfs(root.right)
            
            if left:
                counter += left[1]
            if right:
                counter += right[1]
        

            total_value = left[0] + right[0] + root.val

            maximumAverage = max(total_value/counter, maximumAverage)

            return (total_value, counter) 
        dfs(root)
        return maximumAverage