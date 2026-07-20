class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        memo = [0] * len(nums)
        for i in range(1, len(nums)):
            if i == 1:
                memo[1] = nums[1] - nums[0]
            else:
                memo[i] = memo[i-1] - nums[i-1] + nums[i]
                jon = nums[i] - nums[i-1]
                if jon > memo[i]:
                    memo[i] = jon
            # print(memo)
        ron = max(memo)
        if ron <= 0:
            return -1
        return ron
