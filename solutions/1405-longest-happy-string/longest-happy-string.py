class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        q = []
        if a != 0:
            heapq.heappush(q, (-a, 'a')) #priority, key
        if b != 0:
            heapq.heappush(q, (-b, 'b')) #priority, key
        if c != 0:
            heapq.heappush(q, (-c, 'c')) #priority, key
        out = ''
        while len(q) > 0:
            # cnt, letter = None, None
            if len(out) >= 2 and out[-1] == out[-2] == q[0][1]: # last two are same as most common char
                print(q)
                if len(q) >= 2:
                    cnt, letter = q.pop(1)
                    cnt += 1
                    out += letter
                    if cnt != 0:
                        heapq.heappush(q, (cnt, letter))
                else:
                    break
            else:
                cnt, letter = heapq.heappop(q)
                if cnt == 0:
                    break
                cnt += 1
                out += letter
                heapq.heappush(q, (cnt, letter))
        return out



