class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        len2 = len(nums2)
        len1 = len(nums1)
        dp = [[0]*len2 for _ in range(len1)]
        max_len = 0
        for i in range(len1-1, -1, -1):
            for j in range(len2-1, -1, -1):
                if nums1[i] == nums2[j]:
                    if i+1 < len1 and j+1 < len2:
                        dp[i][j] = 1 + dp[i+1][j+1]
                    # elif i < len2 and j < len1:
                    else:
                        dp[i][j] = 1
                    max_len = max(max_len, dp[i][j]) 
        return max_len
