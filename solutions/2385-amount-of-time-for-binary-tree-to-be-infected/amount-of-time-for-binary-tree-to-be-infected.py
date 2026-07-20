# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # Convert the tree to a graph adjacency list with BFS
        adj = collections.defaultdict(list)
        queue = collections.deque()
        queue.append(root)
        while len(queue) != 0:
            tmp = queue.popleft()
            
            if tmp.left:
                
                adj[tmp.left.val].append(tmp)
                adj[tmp.val].append(tmp.left)
                queue.append(tmp.left)
            if tmp.right:
                adj[tmp.right.val].append(tmp)
                adj[tmp.val].append(tmp.right)
                queue.append(tmp.right)

        # DFS to traverse graph from start point, output max len
        def dfs(prev, curr):
            max_len = 0
            # print(curr, adj[curr])
            for nei in adj[curr]:
                # print(curr, nei.val)
                if nei.val != prev:
                    max_len = max(max_len, 1+dfs(curr, nei.val))
                    # print(curr, nei.val, max_len)
            return max_len
        
        return dfs(start, start)
