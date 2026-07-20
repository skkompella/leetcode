class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # cur_limit = 0
        # furthest = 0
        # for i in range(len(nums)-1):
        #     furthest = i + nums[i]
        #     if cur_limit == i:
        #         cur_limit = furthest
        # if furthest >= len(nums)-1:
        #     return True
        # return False


        furthest = 0
        i = 0
        lenNums = len(nums)-1
        while i <= furthest:
            furthest = max(furthest, i + nums[i])
            i += 1
            if furthest >= lenNums:
                return True
        return False
            
