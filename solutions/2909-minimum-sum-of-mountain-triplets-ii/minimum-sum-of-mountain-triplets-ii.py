class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        l_min = float('inf')
        length = len(nums)
        r_min = r_min = min(nums[2:])
        min_sum = float('inf')
        mins = [0]*length
        mins[-1] = nums[-1]
        for i in range(length-2, -1, -1):
            # print(i)
            mins[i] = min(mins[i+1], nums[i])
        # print(mins)



        for i in range(1, len(nums)-1):
            l_min = min(l_min, nums[i-1])
            # if nums[i] == r_min:
            #     r_min = min(nums[i+1:])
            r_min = mins[i]
            if l_min < nums[i] and r_min < nums[i]:
                min_sum = min(min_sum, l_min + nums[i] + r_min)
        if min_sum == float('inf'):
            return -1
        return min_sum
