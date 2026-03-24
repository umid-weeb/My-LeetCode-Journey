from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_leaf(self,root):
        return not root.left and not root.right
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue =deque([root])
        count=0
        while queue:
            node = queue.pop()
            count+=1
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)
        return count
        