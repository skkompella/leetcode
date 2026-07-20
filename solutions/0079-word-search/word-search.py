class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        length = len(board)
        height = len(board[0])
        word_len = len(word)
        def explore(tup): # run bfs starting from tup
            def explore2(jon, cnt):
                i, j = jon
                if (0 <= i < length) and (0 <= j < height):
                    if cnt < word_len:
                        if board[i][j] == word[cnt]:
                            print(cnt)
                            tmp = board[i][j] 
                            board[i][j] = '#'
                            if cnt == word_len-1:
                                return True
                    
                            res = explore2((i+1, j), cnt+1) or explore2((i, j+1), cnt+1) or explore2((i-1, j), cnt+1) or explore2((i, j-1), cnt+1)
                            board[i][j] = tmp
                            return res
                # print(v)
                # return False
            return explore2(tup, 0)
            
            


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if explore((i, j)) == True:
                        return True
        return False
        


# if (v[-1][0] == i and (j == v[-1][1]+1 or j == v[-1][1]-1)) or (v[-1][1] == j and (i == v[-1][0]+1 or i == v[-1][0]-1)):
#                                     cnt += 1


# def explore(tup): # run bfs starting from tup
#             v = []
#             q = collections.deque()
#             q.append(tup)
#             cnt = 0
#             while q:
#                 jon = q.popleft()
#                 i, j = jon
#                 if jon not in v:
#                     if (0 <= i < length) and (0 <= j < height):
#                         if board[i][j] == word[cnt]:
#                             if len(v) != 0:
#                                 if cnt == word_len:
#                                     return True
#                                 v.append(jon)
#                                 q.appendleft((i+1, j))
#                                 q.appendleft((i, j+1))
#                                 q.appendleft((i-1, j))
#                                 q.appendleft((i, j-1))
#                 print(v)
#             return False
