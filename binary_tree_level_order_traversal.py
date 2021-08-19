# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def levelOrder(self, root):
        opt = []

        if not root: return opt

        q = deque()
        q.append((root, 0))

        while q:
            node, depth = q.popleft()
            if depth<len(opt):
                opt[depth].append(node.val)
            else:
                opt.append([node.val])
            if node.left: q.append((node.left, depth+1))
            if node.right: q.append((node.right, depth+1))
        return opt
