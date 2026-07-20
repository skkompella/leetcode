class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        memo = defaultdict(list)
        memo[0].append("")
        for i in range(1, n+1):
            for j in range(i):
                for left in memo[j]:
                    for right in memo[i-1-j]:
                        memo[i].append("("+left+")"+right)
        return memo[n]
