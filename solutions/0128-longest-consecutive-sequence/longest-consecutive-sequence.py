class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        max_len = 0
        curlen = 0
        for i in seq:
            if i-1 not in seq:
                j = i
                curlen = 0
                while j in seq:
                    curlen += 1
                    j += 1
                max_len = max(max_len, curlen)
        return max_len
