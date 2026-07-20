class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if len(stack) != 0 and stack[-1] == i:
                stack.pop()
                continue
            stack.append(i)
        return "".join(stack)        
        
        
        # while True:
        #     for i in range(len(s)-1):
        #         if s[i] == s[i+1]:
        #             print(s, i)
        #             s = s[:i] + s[i+1:]
        #             print(s)
        #             continue
        #     break
