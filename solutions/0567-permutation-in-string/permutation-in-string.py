class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts_s1 = collections.Counter(s1)
        counts_s2 = collections.Counter(s2[:len(s1)])
        same = 0
        for i in counts_s2.keys():
            if i in counts_s1 and counts_s2[i] == counts_s1[i]:
                same += 1
        if same == len(counts_s1.keys()): return True
        i, j = 1, len(s1)
        while j < len(s2):
            counts_s2[s2[i-1]]-=1
            counts_s2[s2[j]]+=1
            if s2[i-1] != s2[j]:
                if s2[i-1] in counts_s1:
                    if counts_s2[s2[i-1]] == counts_s1[s2[i-1]]:
                        same += 1
                    elif counts_s2[s2[i-1]] == counts_s1[s2[i-1]] - 1:
                        same -= 1
                if s2[j] in counts_s1:
                    if counts_s2[s2[j]] == counts_s1[s2[j]]:
                        same += 1
                    elif counts_s2[s2[j]] == 1 + counts_s1[s2[j]]:
                        same -= 1
            if same == len(counts_s1.keys()): 
                # print(s2[i:j+1])
                return True
            i+=1
            j+=1
        return False

