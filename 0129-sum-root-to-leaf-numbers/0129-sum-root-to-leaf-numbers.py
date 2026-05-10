# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def sumNumbers(self, root: Optional[TreeNode], sum_=0) -> int:
        if not root:
            return 0
        queue = deque([(root, root.val)])
        while queue:
            node, current_val = queue.popleft()
            if not node.left and not node.right:
                sum_ += current_val
            if node.left:
                queue.append((node.left, current_val * 10 + node.left.val))
            if node.right:
                queue.append((node.right, current_val * 10 + node.right.val))
        return sum_
