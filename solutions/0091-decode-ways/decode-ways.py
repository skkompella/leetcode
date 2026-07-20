class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        lenS = len(s)
        letter_set = set(str(i) for i in range(1, 27))
        def recurse(i):
            if i == lenS:
                return 1
            if i not in memo:
                res = 0
                if s[i:i+1] in letter_set:
                    res += recurse(i+1)
                if i+2 <= lenS and s[i:i+2] in letter_set:
                    res += recurse(i+2)
                memo[i] = res
            return memo[i]
        return recurse(0)
