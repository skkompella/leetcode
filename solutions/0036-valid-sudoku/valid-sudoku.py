class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        offsets = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
        for off in offsets:
            li = []
            for i in range(3):
                for j in range(3):
                    if board[i+off[0]][j+off[1]] != '.':
                        if board[i+off[0]][j+off[1]] in li:
                            return False
                        li.append(board[i+off[0]][j+off[1]])
        for row in board:
            li = []
            for i in row:
                if i != '.':
                    if i in li:
                        return False
                    li.append(i)
        for j in range(len(board[0])):
            li = []
            for i in range(len(board)):
                if board[i][j] != '.':
                    if board[i][j] in li:
                        return False
                    li.append(board[i][j])
        return True
