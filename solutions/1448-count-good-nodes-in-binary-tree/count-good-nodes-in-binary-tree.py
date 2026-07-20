# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    cnt = 0
    def recurse(self, root, max_val):
        if root == None:
            return
        if root.val >= max_val:
            self.cnt += 1
            max_val = root.val
        self.recurse(root.left, max_val)
        self.recurse(root.right, max_val)
        
    def goodNodes(self, root: TreeNode) -> int:
        self.recurse(root, root.val)
        return self.cnt
