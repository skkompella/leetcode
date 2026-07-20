class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        max_count = 0
        numZeros = 0
        lenNums = len(nums)
        while r < lenNums:
            jon = nums[r]
            if jon == 1:
                r += 1
                max_count = max(r-l, max_count)
            elif jon == 0:
                if numZeros < k:
                    r += 1
                    numZeros += 1
                    max_count = max(r-l, max_count)
                else:
                    if nums[l] == 0:
                        numZeros -= 1
                        l += 1
                    else:
                        l += 1
        return max_count
        # case 1: next char is a 1
        # case 2: next char is a 0 but you still have k
        # case 3: next char is a 0 and you dont have k
