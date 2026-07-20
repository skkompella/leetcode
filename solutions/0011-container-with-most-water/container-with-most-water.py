class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        lenheight = len(height)
        l, r = 0, lenheight-1
        while l < r and r < lenheight:
            max_water = max(max_water, (r-l)*min(height[l],height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r-=1
        return max_water
