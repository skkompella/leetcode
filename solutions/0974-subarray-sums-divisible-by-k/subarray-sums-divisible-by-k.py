class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_map = defaultdict(int)
        prefix_map[0]+=1
        run_sum = 0
        res = 0

        for i in range(len(nums)):
            run_sum += nums[i]
            res+=prefix_map[run_sum%k]
            prefix_map[run_sum%k]+=1
        return res
