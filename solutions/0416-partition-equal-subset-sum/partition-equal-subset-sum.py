class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        cache = {}
        length = len(nums)
        goal = sum(nums)
        if goal % 2 == 1:
            return False
        goal = goal // 2

        def recurse(i, amt):
            if amt == goal:
                return True
            if i > length-1:
                return False
            if (i, amt) not in cache:
                cache[(i, amt)] = recurse(i+1, amt) or recurse(i+1, amt+nums[i])
            return cache[(i, amt)]
        return recurse(0, 0)
