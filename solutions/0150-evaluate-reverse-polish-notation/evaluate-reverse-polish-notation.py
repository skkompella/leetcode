class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "/":
                s1 = stack.pop()
                s2 = stack.pop()
                # print(s2, tokens[i], s1)
                res = s2/s1
                if res < 0:
                    res = math.ceil(res)
                else:
                    res = math.floor(res)
                stack.append(res)
            elif tokens[i] == "+":
                s1 = stack.pop()
                s2 = stack.pop()
                # print(s1, tokens[i], s2)
                res = s1+s2
                stack.append(res)
            elif tokens[i] == "-":
                s1 = stack.pop()
                s2 = stack.pop()
                # print(s2, tokens[i], s1)
                res = s2-s1
                stack.append(res)
            elif tokens[i] == "*":
                s1 = stack.pop()
                s2 = stack.pop()
                # print(s1, tokens[i], s2)
                res = s1*s2
                stack.append(res)
            else:
                res = int(tokens[i])
                stack.append(int(tokens[i]))
            # print(stack)
        return res
