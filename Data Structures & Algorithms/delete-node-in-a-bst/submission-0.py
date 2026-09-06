# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None

        # deleting the root itself
        if key == root.val:
            # no children
            if not root.left and not root.right:
                return None
            # one child
            elif not root.left or not root.right:
                return root.left or root.right
            # two children
            else:
                successor = root.right

                # find smallest value in right subtree
                while successor.left:
                    successor = successor.left

                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)

                return root

        # key is somewhere on the left
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        # key is somewhere on the right
        else:
            root.right = self.deleteNode(root.right, key)

        return root