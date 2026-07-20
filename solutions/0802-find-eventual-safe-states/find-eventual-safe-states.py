class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Cycle detection from each state
        # for each state do DFS until you get back to that state (maintain visited set)
        # If you see a state again then you are not in a safe node, break
        length = len(graph)
        safe = set()
        unsafe = set()
        def explore(curr, visited):
            if curr in visited:
                unsafe.add(curr)
                return 0
            if curr in unsafe:
                return 0
            if curr in safe:
                return 1
            res = 1
            visited.add(curr)
            for node in graph[curr]:
                if explore(node, visited) == 0:
                    res = 0
                    break
                else:
                    safe.add(node)
            visited.remove(curr)
            if res:
                safe.add(curr)
            else:
                unsafe.add(curr)
            return res
            
        for i in range(length):
            j = explore(i, set())
            if j:
                safe.add(i)
            if not j:
                unsafe.add(i)
        return sorted(list(safe))
