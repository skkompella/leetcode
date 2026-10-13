class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # b -> a
        outgraph = defaultdict(set)
        counts = defaultdict(int)
        for a, b in prerequisites:
            outgraph[b].add(a)
            counts[a]+=1
        
        q = collections.deque()
        for i in range(numCourses):
            if counts[i] == 0:
                q.append(i)
        
        res = []
        while len(q) != 0:
            node = q.popleft()
            res.append(node)
            for nei in outgraph[node]:
                counts[nei]-=1
                if counts[nei] == 0:
                    q.append(nei)
        
        if len(res) == numCourses:
            return res
        return []

