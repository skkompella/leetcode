class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        max_area = 0
        height = len(matrix)
        width = len(matrix[0])
        histogram = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == "1":
                    if i == 0:
                        histogram[i][j] = int(matrix[i][j])
                    else:     
                        histogram[i][j] = histogram[i-1][j]+int(matrix[i][j])

        def max_rectangle(heights):
            heights.append(0)
            stack = []
            max_area = 0
            for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    stack_idx = stack.pop()
                    if stack:
                        idx = stack[-1]
                    else:
                        idx = -1
                    max_area = max(max_area, heights[stack_idx] * (i-idx-1))
                    # if heights[0] == 3:
                    #     print(idx, i, stack_idx, max_area)
                stack.append(i)
            return max_area

        max_area = 0
        for row in histogram:
            j = max_rectangle(row)
            # print(row, j)
            max_area = max(max_area, j)

        return max_area
        # print(histogram)
