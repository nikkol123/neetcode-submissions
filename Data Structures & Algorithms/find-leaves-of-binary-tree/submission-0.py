# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        def getHeight(node: TreeNode | None) -> None:
            if not node:
                return -1

            height = 1 + max(getHeight(node.left), getHeight(node.right))

            #if we encounter an index at the new level we need to allocate the array first
            if height == len(self.res):
                self.res.append([])

            self.res[height].append(node.val)
            return height

        getHeight(root)
        return self.res
            
            
