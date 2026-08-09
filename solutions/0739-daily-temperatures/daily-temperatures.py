class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        temperatures.append(0)
        for i in range(len(temperatures)-1):
            if temperatures[i+1] <= temperatures[i]:
                stack.append(i)
            else:
                res[i] = 1
                while stack and temperatures[i+1] > temperatures[stack[-1]]:
                    tmp_idx = stack.pop()
                    # if tmp_idx == 2:
                    #     print(temperatures[tmp_idx], temperatures[i+1])
                    res[tmp_idx] = i - tmp_idx + 1
            # print(stack)
        return res
