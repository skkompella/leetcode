# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # BFS through the tree to create the adjacency list
        adj = collections.defaultdict(list)
        queue = collections.deque()
        queue.append(root)
        while len(queue) != 0:
            node = queue.popleft()
            if node.left:
                adj[node].append(node.left)
                adj[node.left].append(node)
                queue.append(node.left)
            if node.right:
                adj[node].append(node.right)
                adj[node.right].append(node)
                queue.append(node.right)
        # DFS outward from the node in the adjacency list (distance k)
        res = []
        def dfs(dist, lvn, node):
            if dist == 0:
                res.append(node.val)
                return
            for nei in adj[node]:
                if nei != lvn:
                    dfs(dist-1, node, nei)
            return
        
        dfs(k, target, target)
        return res
