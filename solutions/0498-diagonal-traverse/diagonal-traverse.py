class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # [0, 0], [0, 1], [1, 0], [2, 0], [1, 1], [0, 2]
        # odd, even
        # odd.next is [-1, +1]
        # odd -> check right, if not valid, then down 
        # even.next is [+1, -1]
        # even -> check down, if not valid, then right
        # endif traversed nxn nodes
        n = len(mat) 
        m = len(mat[0])
        cell = [0, 0]
        res = []
        flag = 1 # 1 is odd, 0 is even
        for i in range(n*m):
            # res.append(1 + cell[0]*m + cell[1])
            res.append(mat[cell[0]][cell[1]])
            if flag == 1: # odd
                if 0 <= cell[0]-1 < n and 0 <= cell[1]+1 < m:
                    cell[0] -= 1
                    cell[1] += 1
                    continue
                else:
                    if 0 <= cell[1]+1 < m:
                        cell[1] += 1
                        flag = 0
                        continue
                    else:
                        cell[0] += 1
                        flag = 0
                        continue
            if flag == 0: # even
                if 0 <= cell[0]+1 < n and 0 <= cell[1]-1 < m:
                    cell[0] += 1
                    cell[1] -= 1
                    continue
                else:
                    if 0 <= cell[0]+1 < n:
                        cell[0] += 1
                        flag = 1
                        continue
                    else:
                        cell[1] += 1
                        flag = 1
                        continue
        return res
