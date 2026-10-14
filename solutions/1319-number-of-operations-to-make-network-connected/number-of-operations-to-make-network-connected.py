class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        if len(connections) < n-1:
            return -1
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            p_x = find(x)
            p_y = find(y)
            if p_x != p_y:
                parent[p_y] = p_x
        
        for a, b in connections:
            union(a, b)
        
        for i in range(n):
            find(i)
        
        return len(set(parent))-1
