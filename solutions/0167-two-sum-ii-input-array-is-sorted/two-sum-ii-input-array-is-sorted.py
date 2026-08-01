class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [2, 3, 4]
        # [(0, 4)]
        length = len(numbers)
        lo, hi = 0, length-1
        jon = numbers[lo]+numbers[hi]
        while lo < hi and hi < length:
            if jon == target:
                return [lo+1, hi+1]
            if jon < target: # lo is too small t < hi + lo
                lo += 1
                jon = numbers[lo]+numbers[hi]
            elif jon > target: # hi is too small
                hi -= 1
                jon = numbers[lo]+numbers[hi]
            # print(lo, hi)


            # while i >= 0:
            #     if stack[i][1] == numbers[idx]:
            #         return [stack[i][0]+1, idx+1]
            #     elif stack[i][1] < numbers[idx]:
            #         stack.pop()
            #         i-=1
            #     else:
            #         break
            # stack.append((idx, target-numbers[idx]))
        
        
