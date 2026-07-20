class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_speed = max(piles)
        min_speed = 1
        while max_speed > min_speed:
            mid = (max_speed+min_speed)//2
            time = 0
            for i in piles:
                time += math.ceil(i / mid)
            if time > h:
                min_speed = mid+1
            else:
                max_speed = mid
        return min_speed
