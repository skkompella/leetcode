class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for i in range(len(strs)):
            sorted_i = "".join(sorted(strs[i]))
            # sorted_i = sorted(strs[i])
            if sorted_i not in m:
                m[sorted_i] = [strs[i]]
            else:
                m[sorted_i].append(strs[i])
        return [i for i in m.values()]
