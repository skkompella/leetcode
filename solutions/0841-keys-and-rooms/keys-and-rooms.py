class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        open_rooms = set()
        # DFS with memoization
        def dfs(src):
            if src in open_rooms:
                return
            open_rooms.add(src)
            for room in rooms[src]:
                dfs(room)

        dfs(0)
        return len(open_rooms) == len(rooms)
        
