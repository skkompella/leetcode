class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, = 0, 0
        max_cnt = 0
        sub = {}
        while r < len(s):
            if s[r] not in sub or sub[s[r]] < l: # unique char
                sub[s[r]] = r
                # r+=1
                max_cnt = max(max_cnt, r-l+1)
            else: # s[r] in sub
                l = sub[s[r]] + 1
                sub[s[r]] = r
            r+=1
            # max_cnt = max(max_cnt, r-l)
        return max_cnt
