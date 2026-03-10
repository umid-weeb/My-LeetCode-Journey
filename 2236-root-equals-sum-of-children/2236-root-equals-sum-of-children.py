# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isTrue(self, root):
        if not root or not root.left or not root.right:
            return False
        return  root.val==(root.left.val + root.right.val)
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return self.isTrue(root)
        
        