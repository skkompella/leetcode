class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        length = len(nums)
        def recurse(idx):
            if idx >= length:
                return 0
            if idx not in memo:
                # j1 = nums[idx] + recurse(idx+2)
                # j2 = recurse(idx+1)
                memo[idx] = max(recurse(idx+1), nums[idx] + recurse(idx+2))
            return memo[idx]
        return recurse(0)
