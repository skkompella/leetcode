class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        diffs = {0: 1}
        prefix = 0
        count = 0
        for n in nums:
            prefix += n
            if prefix-k in diffs:
                count += diffs[prefix-k]
            if prefix not in diffs:
                diffs[prefix] = 1
            else:
                diffs[prefix] += 1
        return count               
