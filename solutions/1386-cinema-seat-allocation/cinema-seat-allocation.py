class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = collections.defaultdict(set)
        count = 2*n
        for i,j in reservedSeats:
            seats[i].add(j)
        for idx in seats:
            row = seats[idx]
            if 2 not in row and 3 not in row and 4 not in row and 5 not in row and 6 not in row and 7 not in row and 8 not in row and 9 not in row:
                # count -= 1
                continue
            elif (2 not in row and 3 not in row and 4 not in row and 5 not in row) or (4 not in row and 5 not in row and 6 not in row and 7 not in row) or (6 not in row and 7 not in row and 8 not in row and 9 not in row):
                count -= 1
            else:
                count -= 2
        return count
