class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        p_sum = {}
        run_sum = 0
        res = 0
        p_sum[0] = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                run_sum += 1
            else:
                run_sum -= 1
            if run_sum not in p_sum:
                p_sum[run_sum] = i
            else:
                res = max(res, i-p_sum[run_sum])
        return res
