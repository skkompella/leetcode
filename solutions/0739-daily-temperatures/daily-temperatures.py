class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack:
                if temperatures[stack[-1]] < temperatures[i]:
                    old_temp_idx = stack.pop()
                    res[old_temp_idx] = i-old_temp_idx
                else:
                    break
            stack.append(i)
            # print(stack)
        return res
