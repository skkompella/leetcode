class Solution:
    recurse_map = {}
    def recurse(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        n_minus_one = str(n-1)
        n_minus_two = str(n-2)
        ron = None
        jon = None
        if n_minus_one not in self.recurse_map:
            self.recurse_map[n_minus_one] = self.recurse(n-1)
        if n_minus_two not in self.recurse_map:
            self.recurse_map[n_minus_two] = self.recurse(n-2)
        ron = self.recurse_map[n_minus_one]
        jon = self.recurse_map[n_minus_two]
        return ron + jon
    def climbStairs(self, n: int) -> int:
        return self.recurse(n)
