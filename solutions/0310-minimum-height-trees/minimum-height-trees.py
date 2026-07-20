class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        adj = defaultdict(list)
        degree = [0]*n
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            degree[b]+=1
            degree[a] += 1
        
        q = collections.deque()
        for i in range(n):
            if degree[i] == 1:
                q.append(i)
        res = []
        res.append(list(q))
        while q:
            buffer = []
            for _ in range(len(q)):
                node = q.popleft()
                for nei in adj[node]:
                    degree[nei]-=1
                    if degree[nei] == 1:
                        q.append(nei)
                        buffer.append(nei)
            if buffer:
                res.append(buffer)
        
        return res[-1]
