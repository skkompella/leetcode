class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = [[]]
        for i in nums:
            out_new = [[i] + el for el in out]
            out.extend(out_new)
        return out
