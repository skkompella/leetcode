class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = {}

        q = collections.deque()
        i = 0
        for i in range(len(graph)):
            # if graph[i] == []:
                
            if i in visited:
                continue
            q.append(i) # color, node
            visited[i] = 1

            while q:
                node = q.popleft()
                for v in graph[node]:
                    if v not in visited:
                        visited[v] = -visited[node]
                        q.append(v)
                    else:
                        if visited[node] == visited[v]:
                            return False
        
        return True
            
