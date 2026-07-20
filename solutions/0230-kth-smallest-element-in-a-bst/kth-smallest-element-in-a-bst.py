# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    smallest = []
    def recurse(self, root):
        if root == None:
            return
        self.recurse(root.left)
        self.smallest.append(root.val)
        self.recurse(root.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.smallest = []
        self.recurse(root)
        return self.smallest[k-1]
