class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if len(s) == 1:
            return s[0]
        if len(s)==2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        
        memo = [[False] * n for _ in range(n)]
        start = 0
        max_len = 0
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j-i <= 2 or memo[i+1][j-1] == True):
                    memo[i][j] = True
                    if max_len < (j-i+1):
                        start = i
                        max_len = j-i+1
        return s[start:start+max_len]
        
