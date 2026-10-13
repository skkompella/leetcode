class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # topological ordering
        # init queue with nodes with no parents
        # if you can run thru all nodes, success, else failure
        # b -> a
        outgraph = defaultdict(set)
        counts = defaultdict(int)
        for a, b in prerequisites:
            outgraph[b].add(a)
            counts[a]+=1
        
        q = collections.deque()
        for c in range(numCourses):
            if counts[c] == 0:
                q.append(c)
        
        res = 0
        while len(q) != 0:
            res+=1
            node = q.popleft()
            for n in outgraph[node]:
                counts[n]-=1
                if counts[n]==0:
                    q.append(n)
        # print(res)
        return res==numCourses
