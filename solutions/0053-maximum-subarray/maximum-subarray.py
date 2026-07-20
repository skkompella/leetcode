class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = nums[0]
        best = nums[0]
        for i in range(1, len(nums)):
            if memo < 0:
                memo = nums[i]
            else:
                memo = memo+nums[i]
            best = max(best, memo)
        return best
