class Solution:
    def findMin(self, nums: List[int]) -> int:
        running_min = float('inf')
        
        def binsearch(i, j):  
            if j-i == 0:
                return nums[i]
            elif j-i == 1:
                return min(nums[i], nums[j])
            mid = (i+j)//2
            # print(i, j, mid)
            min_val = nums[mid]
            print(nums[mid], nums[i], nums[j], mid)
            if nums[mid] < nums[j]:
                # min value is either mid or the other half
                # print(nums[mid])
                min_val = min(min_val, binsearch(i, mid))
            elif nums[mid] > nums[i]:
                min_val = nums[i]
                min_val = min(min_val, binsearch(mid, j))
            return min_val
        return binsearch(0, len(nums)-1)
