class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        l1 = len(word1)
        l2 = len(word2)
        def recurse(i_1, i_2):
            if i_1 == l1: return l2-i_2
            if i_2 == l2: return l1-i_1
            if (i_1, i_2) in memo: return memo[(i_1, i_2)]

            if word1[i_1] == word2[i_2]: 
                memo[(i_1, i_2)] = recurse(i_1+1, i_2+1)
            else:
                insert = 1 + recurse(i_1, i_2+1)
                delete = 1 + recurse(i_1+1, i_2)
                replace = 1 + recurse(i_1+1, i_2+1)
                memo[(i_1, i_2)] = min(insert, delete, replace)
            return memo[(i_1, i_2)]

        return recurse(0, 0)
