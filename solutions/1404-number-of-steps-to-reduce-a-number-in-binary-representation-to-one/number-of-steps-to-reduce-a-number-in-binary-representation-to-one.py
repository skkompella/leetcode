class Solution:
    def numSteps(self, s: str) -> int:
        cnt = 0
        carry = 0
        for i in range(len(s)-1, 0, -1): # for each digit except MSB 1
            if carry+int(s[i]) == 1: # if carry + digit == 1 then you are adding 2 to count
                cnt += 2 # 1 + 0 or 0 + 1
                carry = 1 # make carry 1
            else: # 1 + 1 or 0 + 0
                cnt += 1
        return cnt+carry # remember
