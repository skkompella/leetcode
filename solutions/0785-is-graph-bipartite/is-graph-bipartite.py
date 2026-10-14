class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = {}
        def helper(start):
            if start in visited:
                return 1
            visited[start] = 1
            q = collections.deque()
            q.append(start)
            while len(q) != 0:
                # prev *= -1
                for _ in range(len(q)):
                    node = q.popleft()
                    # visited[node] = prev
                    for nei in graph[node]:
                        if nei in visited:
                            if visited[nei] == visited[node]:
                                return 0
                        else:
                            visited[nei] = -visited[node]
                            q.append(nei)
            return 1
        
        for n in range(len(graph)):
            if helper(n) == 0:
                return False
        return True
