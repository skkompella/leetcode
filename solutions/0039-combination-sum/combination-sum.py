class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        ron = []
        def dfs(li, num):
            if num == 0:
                out.append(li)
                return
            if num < 0:
                return
            for i in candidates:
                if li != ron and li[-1] < i:
                    continue
                jon = li[:]
                jon.append(i)
                # if jon in out:
                #     continue
                dfs(jon, num-i)
        dfs([], target)
        return out
