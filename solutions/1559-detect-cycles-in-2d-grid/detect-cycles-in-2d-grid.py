class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # DFS, start at one node, traverse to available cardinal directions
        # keep track of last visited node, mark visited nodes in the grid
        # if length >= 4 and you see a visited node (adjacent) that is not lvn, break
        gridlen = len(grid)
        gridheight = len(grid[0])
        def dfs(lvn_x, lvn_y, x, y, len, char):
            for i, j in ((0,1), (0,-1), (1,0), (-1,0)):
                tmp_x, tmp_y = i+x, j+y
                if 0 <= tmp_x < gridlen and 0 <= tmp_y < gridheight:
                    if tmp_x != lvn_x or tmp_y != lvn_y:
                        if len >= 4:
                            # check for a # or continue to next case
                            if grid[tmp_x][tmp_y] == char.upper():
                                return True
                        if grid[tmp_x][tmp_y] == char:
                            grid[tmp_x][tmp_y] = char.upper()
                            if dfs(x, y, tmp_x, tmp_y, len+1, char) == True:
                                return True
                            # grid[tmp_x][tmp_y] = char
        
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if dfs(i, j, i, j, 1, grid[i][j]) == True:
        #             return True
        # return False

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j].islower():          # skip already-visited
                    char = grid[i][j]
                    grid[i][j] = char.upper()     # mark start before recursing
                    if dfs(i, j, i, j, 1, char):  # pass lowercase char
                        return True
        return False
