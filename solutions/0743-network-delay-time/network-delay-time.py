class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = defaultdict(int)
        visited[k] = 0

        adj = defaultdict(list)
        weights = {}
        for u, v, w in times:
            adj[u].append(v)
            weights[(u, v)] = w
        
        heap = []
        for connect in adj[k]:
            heapq.heappush(heap, (weights[(k, connect)], k, connect))
        # print(heap)
        while heap:
            weight, u, v = heapq.heappop(heap)
            if v in visited:
                continue
            visited[v] = weight
            for node in adj[v]:
                if node not in visited:
                    # print(v, node, visited[v] + weights[(v, node)], visited)
                    heapq.heappush(heap, (weight + weights[(v, node)], v, node))
        
        # print(visited)
        j = visited.values()
        if len(j) != n:
            return -1
        return max(j)
