class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def recurse(i_1, i_2):
            if (i_1, i_2) in memo:
                return memo[(i_1, i_2)]
            if i_1 < len(text1) and i_2 < len(text2):
                if text1[i_1] == text2[i_2]:
                    memo[(i_1, i_2)] = 1+recurse(i_1+1, i_2+1)
                else:
                    memo[(i_1, i_2)] = max(recurse(i_1+1, i_2), recurse(i_1, i_2+1))
                return memo[(i_1, i_2)]
            return 0
        return recurse(0, 0)
