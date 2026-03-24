# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def symmetric(self, men, sen):
        if not men and not sen:
            return True
        if not men or not sen:
            return False
        if men.val != sen.val:
            return False
        return self.symmetric(men.left, sen.right) and \
        self.symmetric(men.right, sen.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.symmetric(root, root)

        