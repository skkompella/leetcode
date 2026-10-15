class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)-1
        for i in range(len(matrix)//2):
            for j in range(i, length-i):
                # print(matrix[i][j], matrix[j][length-i], matrix[length-i][length-j], matrix[length-j][i])
                matrix[i][j], matrix[j][length-i], matrix[length-i][length-j], matrix[length-j][i] = matrix[length-j][i], matrix[i][j], matrix[j][length-i], matrix[length-i][length-j]
                # print(matrix[i][j], matrix[j][length-i], matrix[length-i][length-j], matrix[length-j][i])
                # print(matrix[i][j])
