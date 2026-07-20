class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        table = {}
        for i, (a, b) in enumerate(equations):
            adj[a].append(b)
            adj[b].append(a)
            table[(a, b)] = values[i]
            table[(b, a)] = 1/values[i]
        
        def dfs(source, dest, visited):
            visited.add(source)
            for node in adj[source]:
                if node not in visited:
                    if node == dest:
                        return table[(source, node)]
                    res = dfs(node, dest, visited)
                    if res != -1:
                        return res * table[(source, node)]
            return -1

        res = []
        for i, j in queries:
            if i not in adj or j not in adj:
                res.append(-1.0)
            elif i == j:
                res.append(1.0)
            else:
                jon = set()
                res.append(dfs(i, j, jon))
        return res
