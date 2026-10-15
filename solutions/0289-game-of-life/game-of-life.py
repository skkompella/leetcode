class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # encode 2 as future live past dead, 3 as future dead past live
        # encode 1 as future live past live, 0 as future dead, past dead
        length = len(board)
        height = len(board[0])
        def neighbors(i, j):
            live_count=0
            for x, y in [(1, 0), (1, 1), (0, 1), (0, -1), (-1, -1), (1, -1), (-1, 1), (-1, 0)]:
                nx, ny = i+x, j+y
                if 0 <= nx < length and 0 <= ny < height:
                    if board[nx][ny] == 1 or board[nx][ny] == 3:
                        live_count+=1
            if board[i][j] == 1 and live_count < 2:
                board[i][j] = 3
            # elif board[i][j] == 1 and (live_count == 2 or live_count == 3):
            #     board[i][j] = 2
            elif board[i][j] == 1 and live_count > 3:
                board[i][j] = 3
            elif board[i][j] == 0 and live_count == 3:
                board[i][j] = 2

        for i in range(len(board)):
            for j in range(len(board[0])):
                neighbors(i, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == 3:
                    board[i][j] = 0
