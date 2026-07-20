# class Solution:
#     def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # DFS from path to destination
        # Every call of the recursive function has a visited set
        # def recurse(src, dest):
        #     if src == dest:
        #         return [[src]]
        #     res = []
        #     for node in graph[src]:
        #         j = recurse(node, dest)
        #         if j:
        #             for r in j:
        #                 res.append([src]+r)
        #     return res
        # return recurse(0, len(graph)-1)
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []
        path = []

        def recurse(src):
            path.append(src)
            if src == n - 1:
                res.append(path[:])
            else:
                for node in graph[src]:
                    recurse(node)
            path.pop()

        recurse(0)
        return res
        
        
