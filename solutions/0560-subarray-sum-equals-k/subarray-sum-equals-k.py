class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        run_sum = 0
        tot = 0
        for i in nums:
            run_sum += i
            if run_sum-k in seen:
                # print()
                tot+=seen[run_sum-k]
            seen[run_sum]+=1
        return tot
