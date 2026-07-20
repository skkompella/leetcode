class Solution:
    def countBits(self, n: int) -> List[int]:
        def countJits(n):
            cnt = 0
            while n > 0:
                if n % 2 == 1:
                    cnt += 1
                n = n >> 1
            return cnt
        jon = []
        for i in range(n+1):
            jon.append(countJits(i))
        return jon
