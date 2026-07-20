class Solution:
    # def maxProduct(self, nums: List[int]) -> int:
    #     dp = nums[0]
    #     pos_running_product = nums[0]
    #     min_running_product = nums[0]
    #     for i in range(1, len(nums)):
    #         # print(running_product, nums[i], dp[i-1])
    #         tmp1 = pos_running_product * nums[i]
    #         tmp2 = min_running_product * nums[i]
    #         pos_running_product = max(tmp1, tmp2, nums[i])
    #         min_running_product = min(tmp1, tmp2, nums[i])
    #         dp = max(dp, pos_running_product)
    #     return dp
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            candidates = (nums[i], max_so_far * nums[i], min_so_far * nums[i])
            max_so_far = max(candidates)
            min_so_far = min(candidates)
            result = max(result, max_so_far)
        return result
