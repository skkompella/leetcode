class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        res = [[0]*len(img[0]) for _ in range(len(img))]
        height = len(img)
        width = len(img[0])

        def sum_func(i, j):
            s, tot = 0, 0
            for x, y in [(0, 0), (0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]:
                n_x, n_y = i+x, j+y
                if 0 <= n_x < height and 0 <= n_y < width:
                    s += img[n_x][n_y]
                    tot += 1
            return s//tot


        for i in range(height):
            for j in range(width):
                res[i][j] = sum_func(i, j)
        return res
