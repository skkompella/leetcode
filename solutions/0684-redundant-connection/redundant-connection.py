class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for i, j in edges:
            p_x, p_y = find(i), find(j)
            if p_x == p_y:
                return [i, j]
            parent[p_x] = p_y
