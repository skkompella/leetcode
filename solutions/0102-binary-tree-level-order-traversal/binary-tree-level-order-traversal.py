# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversal = []
        q = collections.deque()
        q.append(root)
        if not root:
            return []
        while len(q) != 0:
            level = []
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                # if node:
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            traversal.append(level)
        return traversal

