class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        lenStr = len(s3)
        lenStr1 = len(s1)
        lenStr2 = len(s2)
        if lenStr1 + lenStr2 != lenStr:
            return False
        def recurse(i, j):
            if i > lenStr1 or j > lenStr2:
                return False
            if i+j == lenStr:
                return True
            if (i, j) not in memo:
                res = False
                if i < lenStr1 and s3[i+j] == s1[i]:
                    res = res or recurse(i+1, j)
                if j < lenStr2 and s3[i+j] == s2[j]:
                    res = res or recurse(i, j+1)
                memo[(i,j)] = res

            return memo[(i, j)]
        return recurse(0, 0)
