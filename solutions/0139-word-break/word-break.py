class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_lengths = sorted(set(len(w) for w in wordDict))
        word_set = sorted(set(w for w in wordDict))
        memo = {}
        length = len(s)
        def recurse(idx):
            if idx > length:
                return 0
            if idx == length:
                return True
            if idx not in memo:
                res = False
                for l in word_lengths:
                    if s[idx:idx+l] in word_set:
                        res = res or recurse(idx+l)
                memo[idx] = res
            return memo[idx]
        return recurse(0)
