class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_map = {0:-1}
        run_sum = 0

        for i in range(len(nums)):
            run_sum += nums[i]
            if run_sum%k not in prefix_map:
                prefix_map[run_sum%k] = i
            else:
                if i - prefix_map[run_sum%k] > 1:
                    return True
        return False
