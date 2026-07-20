class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        run = 1
        for i in range(len(nums)):
            output[i] *= run
            run *= nums[i]
        # print(output)
        run = 1
        # print(len(nums))
        for j in range(len(nums)-1, -1, -1):
            # print(output[j], run)
            output[j] *= run
            run *= nums[j]
        return output
