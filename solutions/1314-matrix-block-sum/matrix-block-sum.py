class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        height = len(mat)
        width = len(mat[0])
        prefix = [[0]*(width+1) for _ in range(height+1)]

        for i in range(1, height+1):
            for j in range(1, width+1):
                prefix[i][j] = mat[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
        print(prefix)
        
        def mbs(i, j):
            # naive formula: prefix[i+k][j+k] - prefix[i-k][j] - prefix[i][j-k] + prefix[i-k][j-k]
            u_i, u_j, l_i, l_j = 1+min(i+k, height-1), 1+min(width-1, j+k), max(0, i-k), max(0, j-k)
            return prefix[u_i][u_j] - prefix[l_i][u_j] - prefix[u_i][l_j] + prefix[l_i][l_j]

        answer = [[0]*(width) for _ in range(height)]
        for i in range(height):
            for j in range(width):
                answer[i][j] = mbs(i, j)
        
        return answer
