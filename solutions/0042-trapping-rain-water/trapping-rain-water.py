class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = []
        right_max = []
        max_height = 0
        for i in range(len(height)):
            left_max.append(max_height)
            max_height = max(max_height, height[i])
        max_height=0
        for i in range(len(height)-1, -1, -1):
            right_max.insert(0, max_height)
            max_height = max(max_height, height[i])
        
        # print(left_max)
        # print(right_max)
        # debug = []
        res=0
        for i in range(len(height)):
            # debug.append(max(0, min(left_max[i]-height[i], right_max[i]-height[i])))
            res += max(0, min(left_max[i]-height[i], right_max[i]-height[i]))
        # print(debug)
        return res
