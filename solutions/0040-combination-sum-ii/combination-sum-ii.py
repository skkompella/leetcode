class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        out = []
        lenght = len(candidates)
        def dfs(li, pointer, tar):
            if tar == 0:
                out.append(li)
                return
            if tar < 0:
                return
            for i in range(pointer, lenght):
                if i > pointer and candidates[i] == candidates[i-1]:
                    continue
                jon = li[:]
                jon.append(candidates[i])
                dfs(jon, i+1, tar-candidates[i])
        dfs([], 0, target)
        return out
