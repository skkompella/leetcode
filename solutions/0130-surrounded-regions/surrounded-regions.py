class Solution:
    def solve(self, board: List[List[str]]) -> None:
        height = len(board)
        width = len(board[0])
        q = collections.deque()
        for i in range(height):
            for j in range(width):
                if i == height-1 or i == 0 or j == width-1 or j == 0:
                    if board[i][j] == 'O':
                        board[i][j] = '1'
                        q.append((i, j))

        while len(q) != 0:
            jon = q.popleft()
            i, j = jon[0], jon[1]
            if (0 <= i+1 < height and 0 <= j < width):
                if board[i+1][j] == 'O':
                    board[i+1][j] = '1'
                    q.append((i+1, j))
            if (0 <= i-1 < height and 0 <= j < width):
                if board[i-1][j] == 'O':
                    board[i-1][j] = '1'
                    q.append((i-1, j))
            if (0 <= i < height and 0 <= j+1 < width):
                if board[i][j+1] == 'O':
                    board[i][j+1] = '1'
                    q.append((i, j+1))
            if (0 <= i < height and 0 <= j-1 < width):
                if board[i][j-1] == 'O':
                    board[i][j-1] = '1'
                    q.append((i, j-1))
        
        for i in range(height):
            for j in range(width):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(height):
            for j in range(width):
                if board[i][j] == '1':
                    board[i][j] = 'O'
