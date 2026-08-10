class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # print(matrix)
        length = len(matrix)-1
        for k in (range(len(matrix)//2)):
            for i in range(k, length-k):
                # if k == 1:
                    # print(matrix[k][i], matrix[i][length-k], matrix[length-k][length-i], matrix[length-i][k])
                matrix[k][i], matrix[i][length-k], matrix[length-k][length-i], matrix[length-i][k] = matrix[length-i][k], matrix[k][i], matrix[i][length-k], matrix[length-k][length-i]
            # length -= 1
                # print(matrix)
            #     break
            # print(matrix)
            # break
