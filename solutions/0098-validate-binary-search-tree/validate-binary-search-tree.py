# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # is_bst = True
    # def recurse(self, root, leftbound, rightbound):
    #     if self.is_bst == False:
    #         return
    #     if root == None:
    #         return
    #     if root.val <= leftbound or root.val >= rightbound:
    #         self.is_bst = False
    #     self.recurse(root.left, leftbound, root.val)
    #     self.recurse(root.right, root.val, rightbound)

    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     self.is_bst = True
    #     if root == None:
    #         return True
    #     if root.left == None and root.right == None:
    #         return True
    #     self.recurse(root.left, -2e31-1, root.val)
    #     self.recurse(root.right, root.val, 2e31+1)
    #     return self.is_bst
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False

            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))
        
