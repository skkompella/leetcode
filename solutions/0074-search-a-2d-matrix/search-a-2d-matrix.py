class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # binary search on the matrix, row by row
        m = len(matrix)
        n = len(matrix[0])

        def translate(idx):
            return (idx//n, idx%n)
        
        lo, hi = 0, m*n-1
        while lo <= hi:
            mid = (lo+hi)//2
            i, j = translate(mid)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                hi = mid-1
            else:
                lo = mid+1
        # i, j = translate(lo)
        # if matrix[i][j] == target:
        #     return True
        return False
