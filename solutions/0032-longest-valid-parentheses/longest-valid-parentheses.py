class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                jon = stack.pop()
                if not stack:
                    max_len = max(max_len, i-jon-1)
                    stack.append(i)
                else:
                    max_len = max(max_len, i-stack[-1]) 
                    # continue
            # print(stack)
        return max_len
