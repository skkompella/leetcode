class Solution:
    def rob(self, nums: list[int]) -> int:
        cache = {}
        length = len(nums)
        def recurse(i):
            if i > length-1:
                return 0
            if i not in cache:
                cache[i] = max(recurse(i+1), nums[i]+recurse(i+2))
            return cache[i]
        return recurse(0)
        
