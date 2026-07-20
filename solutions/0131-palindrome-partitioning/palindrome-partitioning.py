class Solution:
    def partition(self, s: str) -> List[List[str]]:
        memo = defaultdict(list)
        length = len(s)
        def isPalindrome(buf):
            if buf == buf[::-1]:
                return True
            return False

        def recurse(idx):
            if idx >= length:
                return [[]]
            if idx not in memo:
                for i in range(idx+1, length+1):
                    if isPalindrome(s[idx:i]):
                        tmp = recurse(i)
                        for j in tmp:
                            memo[idx].append([s[idx:i]] + j)
            return memo[idx]
        return recurse(0)
