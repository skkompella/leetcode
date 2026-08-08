class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_rect = 0
        heights.append(0)
        for i in range(len(heights)):
            # min_height = float('inf')
            while stack and heights[i] < stack[-1][0]:
                height, _ = stack.pop()
                if not stack:
                    l_idx = -1
                else:
                    l_idx = stack[-1][1]
                # print(i, l_idx)
                # min_height = min(min_height, height)
                max_rect = max(max_rect, height * (i-l_idx-1))
            stack.append((heights[i], i))
            # print(stack)
        return max_rect
