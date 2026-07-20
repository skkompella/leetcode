class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # m = {}
        # l, r = 0, 0
        # max_len = 0
        # max_freq = 0
        # s = s+'#'
        # while r < len(s):
        #     min_rep = (r-l) - (max_freq if len(m) != 0 else 0)
        #     if min_rep <= k:
        #         if s[r] not in m:
        #             m[s[r]] = 1
        #         else:
        #             m[s[r]] += 1
        #         max_freq = max(max_freq, m[s[r]])
        #         r += 1
        #         max_len = max(max_len, r-l-1)
        #     else:
        #         m[s[l]] -= 1
        #         l += 1
            
        # return max_len

        from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        max_freq = 0
        result = 0

        for r in range(len(s)):
            count[s[r]] += 1
            max_freq = max(max_freq, count[s[r]])

            if (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)

        return result
