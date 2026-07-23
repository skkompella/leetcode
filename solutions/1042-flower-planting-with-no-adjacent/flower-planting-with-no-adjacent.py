class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for x, y in paths:
            adj[x].append(y)
            adj[y].append(x)
        # print(adj)

        visited = {}
        for node in range(1, n+1):
            avail = {1,2,3,4}
            for nei in adj[node]:
                if nei in visited:
                    avail.discard(visited[nei])
            visited[node] = avail.pop()


        return [visited[i] for i in range(1, n+1)]
