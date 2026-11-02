class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder.sort()
        res = [folder[0]]
        prev = folder[0]
        for i in range(1, len(folder)):
            if prev != folder[i][:len(prev)] or (len(folder[i]) <= len(prev) or folder[i][len(prev)] != '/'):
                prev = folder[i]
                res.append(folder[i])
        return res
