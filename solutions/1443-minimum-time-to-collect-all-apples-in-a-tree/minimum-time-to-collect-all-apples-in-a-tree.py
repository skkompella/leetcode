class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = {}
        for i in edges:
            if i[0] not in tree:
                tree[i[0]] = []
            if i[1] not in tree:
                tree[i[1]] = []
            tree[i[0]].append(i[1])
            tree[i[1]].append(i[0])

        visited = set()
        def dfs(node, parent):
            s = 0
            if node not in tree:
                return 0
            for child in tree[node]:
                if child != parent:
                    ch = dfs(child, node)
                    if ch > 0 or hasApple[child]:
                        s += 2 + ch
                
            
            return s
        
        return dfs(0, -1)


