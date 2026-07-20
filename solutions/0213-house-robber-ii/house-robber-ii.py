class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        
        def hrob(houses):
            curr, prev = 0, 0
            for i in houses:
                prev, curr = curr, max(prev+i, curr)
            return curr
        return max(hrob(nums[1:]), hrob(nums[:-1]))
