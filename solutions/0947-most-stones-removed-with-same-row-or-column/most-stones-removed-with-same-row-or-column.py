class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        for x, y in stones:
            y_enc = y+10001
            # if x not in parent and y_enc in parent:
            #     parent[find(x)] = parent[find(y_enc)]
            # else:
            p_x, p_y = find(x), find(y_enc)
            if p_x != p_y:
                parent[p_y] = p_x
            # print(parent)
        
        # for x, _ in stones:
        #     find(x)
        # print(parent)
        roots = set(find(x) for x, y in stones)
        return len(stones)-len(roots)



