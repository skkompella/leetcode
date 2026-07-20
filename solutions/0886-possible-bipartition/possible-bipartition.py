class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in dislikes:
            adj[a].append(b)
            adj[b].append(a)
        visited = {} # 0 for red 1 for blue
        # print(adj)

        def bfs(src):
            if src in visited:
                return True
            q = collections.deque()
            q.append((src, 1))
            visited[src] = 1
            while q:
                node, color = q.popleft()
                for nei in adj[node]:
                    if nei not in visited:
                        visited[nei] = -color
                        q.append((nei, -color))
                    else:
                        if visited[nei] != -color:
                            return False
            return True
        
        for i in range(1, n+1):
            if not bfs(i):
                return False
        return True

