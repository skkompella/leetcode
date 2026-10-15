class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        t_map = collections.Counter(t)
        req = len(t_map)
        i = 0
        s_map = collections.Counter()
        same = 0
        min_set = None

        for j, c in enumerate(s):
            s_map[c] += 1
            if c in t_map and s_map[c] == t_map[c]:
                same += 1
            while same == req:
                if min_set is None or (j - i + 1) < len(min_set):
                    min_set = s[i:j+1]
                left = s[i]
                if left in t_map and s_map[left] == t_map[left]:
                    same -= 1
                s_map[left] -= 1
                i += 1
        return "" if min_set is None else min_set
