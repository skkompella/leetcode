class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        running_xor = 0
        for i in nums:
            running_xor = i ^ running_xor
        return running_xor
