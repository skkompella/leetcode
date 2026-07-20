class Solution:
    def reverseWords(self, s: str) -> str:
        jon = s.split()
        jon.reverse()
        return " ".join(jon)
