# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = defaultdict(list)
        def recurse(lower, upper):
            if (lower, upper) not in memo:
                if lower > upper:
                    return [None]
                if lower == upper:
                    return [TreeNode(lower)]
                for k in range(lower, upper+1):
                    # left: lower - k-1
                    # right: k+1 - upper
                    tree = TreeNode(k)
                    leftTreeList = recurse(lower, k-1)
                    rightTreeList = recurse(k+1, upper)
                    for i in leftTreeList:
                        for j in rightTreeList:
                            tree = TreeNode(k)
                            tree.left = i
                            tree.right = j
                            memo[(lower, upper)].append(tree)
            return memo[(lower, upper)]
        return recurse(1, n)
