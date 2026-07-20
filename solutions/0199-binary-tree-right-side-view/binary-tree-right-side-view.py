# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    li = []
    def lingesh(self, root, height):
        if root == None:
            return
        if len(self.li) < height:
            self.li.append(root.val)
        self.lingesh(root.right, height+1)
        self.lingesh(root.left, height+1)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.li = []
        self.lingesh(root, 1)
        return self.li
