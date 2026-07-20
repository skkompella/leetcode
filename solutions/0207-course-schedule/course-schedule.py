class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        indegrees = [0] * numCourses
        for course, prereq in prerequisites:
            adj[prereq].append(course) # b -> a in the graph
            indegrees[course] += 1
        queue = collections.deque([i for i in range(numCourses) if indegrees[i] == 0])
        while len(queue) != 0:
            prereq = queue.popleft()
            for course in adj[prereq]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    queue.append(course)
        for i in indegrees:
            if i != 0:
                return False
        return True
