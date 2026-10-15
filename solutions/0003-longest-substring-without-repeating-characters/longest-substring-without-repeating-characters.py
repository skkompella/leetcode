class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = 0
        uniques = set()

        i = 0
        for j in range(len(s)):
            while s[j] in uniques:
                uniques.discard(s[i])
                i+=1
            uniques.add(s[j])
            sub = max(sub, len(uniques))
        
        return sub
