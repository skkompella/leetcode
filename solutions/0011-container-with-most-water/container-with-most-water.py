class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_height = 0
        i, j = 0, len(height)-1
        while i < j:
            max_height = max(max_height, (j-i)*min(height[i], height[j]))
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return max_height
