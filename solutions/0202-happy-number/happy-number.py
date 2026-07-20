class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            s = 0
            while n > 0:
                s += (n%10)**2
                n=n//10
            if s==1:
                return True
            if s in seen:
                return False
            seen.add(s)
            n = s
