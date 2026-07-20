class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hset = {target-nums[i]:i for i in range(len(nums))}
        for i in range(len(nums)):
            if nums[i] in hset and hset[nums[i]]!=i:
                return [i, hset[nums[i]]]
        return res
