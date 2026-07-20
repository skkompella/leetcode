class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # parent = [i for i in range(len(isConnected))]
        n = len(isConnected)
        parent = [-1]*n
        
        def bfs(idx):
            q = collections.deque()
            q.append(idx)
            while q:
                node = q.popleft()
                for connection in range(n):
                    if isConnected[node][connection] == 1 and parent[connection] != parent[node]:
                        parent[connection] = parent[node]
                        q.append(connection)
        
        for i in range(n):
            if parent[i] == -1:
                print(i)
                parent[i] = i
                bfs(i)
        print(parent)
        return len(set(parent))
