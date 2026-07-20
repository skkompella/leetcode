class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)] # prereq : [courses]
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        
        q = collections.deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        
        print(graph)
        print(in_degree)

        visited = []
        # v = 0
        while len(q) != 0:
            i = q.popleft()
            # v += 1
            visited.append(i)
            for c in graph[i]:
                in_degree[c] -= 1
                if in_degree[c] == 0:
                    q.append(c)
        if len(visited) == numCourses:
            return visited
        return []
