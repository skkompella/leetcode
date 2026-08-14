class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        sort = []
        length, width = len(mat), len(mat[0])
        i, j = length-1, 0
        def check(i, j):
            if 0 <= i < length and 0 <= j < width:
                return True
            return False
        # print(i, j, width-1, i!=0 and j!=width-1)
        while not (i == 0 and j == width-1):
            bucket = []
            i_0, j_0 = i, j
            while check(i, j):
                bucket.append(mat[i][j])
                i, j = i+1, j+1
            bucket.sort()
            # print(bucket)
            # print(i, j, width)
            i, j = i_0, j_0
            for el in bucket:
                mat[i_0][j_0] = el
                i_0, j_0 = i_0+1, j_0+1
            # print(i, j)
            if check(i-1, j):
                i-=1
            else:
                j+=1
        
        return mat
