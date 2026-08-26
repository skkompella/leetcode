class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        same = 0
        res = []
        counts_p = collections.Counter(p)
        counts_s = collections.Counter(s[:len(p)])
        for c in counts_s:
            if c in counts_p and counts_s[c] == counts_p[c]:
                same += 1
        # print(same)
        if same == len(counts_p): res.append(0)

        i, j = 1, len(p)
        while j < len(s):
            out_c, in_c = s[i-1], s[j]
            counts_s[out_c] -= 1
            counts_s[in_c] += 1
            if out_c != in_c:                       # nothing changed if equal
                if out_c in counts_p:
                    if counts_s[out_c] == counts_p[out_c]:     same += 1
                    elif counts_s[out_c] == counts_p[out_c]-1: same -= 1
                if in_c in counts_p:
                    if counts_s[in_c] == counts_p[in_c]:       same += 1
                    elif counts_s[in_c] == counts_p[in_c]+1:   same -= 1
            if same == len(counts_p): res.append(i)
            i += 1
            j += 1
        return res
