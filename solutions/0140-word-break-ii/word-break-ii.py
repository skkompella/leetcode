class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_lengths = sorted(set(len(w) for w in wordDict))
        word_set = sorted(set(w for w in wordDict))
        memo = {}
        length = len(s)
        def recurse(idx):
            if idx == length:
                return [[]]
            if idx not in memo:
                res = []
                for l in word_lengths:
                    tmp = s[idx:idx+l]
                    if tmp in word_set:
                        r = recurse(idx+l)
                        for el in r:
                            res.append([tmp]+el)
                memo[idx] = res
            return memo[idx]
        return [" ".join(words) for words in recurse(0)]
