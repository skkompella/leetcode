class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        length, width = len(mat), len(mat[0])
        i, j = 0, 0
        def check(i, j):
            if 0 <= i < length and 0 <= j < width:
                return True
            return False

        while True:
            res.append(mat[i][j])
            while check(i-1, j+1):
                i-=1
                j+=1
                res.append(mat[i][j])
                # print(mat[i][j])
            if check(i, j+1):
                j+=1
                res.append(mat[i][j])
            elif check(i+1, j):
                i+=1
                res.append(mat[i][j])
            # print(mat[i][j])
            else:
                break
            while check(i+1, j-1):
                i+=1
                j-=1
                res.append(mat[i][j])
                # print(mat[i][j])
            if check(i+1, j):
                i+=1
                # res.append(mat[i][j])
            elif check(i, j+1):
                j+=1
                # res.append(mat[i][j])
            # print(mat[i][j])
            else:
                break
            # break
        return res
