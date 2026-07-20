class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # heap for least used tasks
        counts = collections.Counter(tasks)
        heap = [(-cnt) for cnt in counts.values()]
        heapq.heapify(heap)
        # queue for cooldowns
        q = collections.deque()
        time = 0
        # keep going until counts are all 0
        while heap or q:
            time += 1
            if heap:
                c = heapq.heappop(heap) + 1
                if c != 0:
                    q.append((time+n, c))
            if q and q[0][0]==time:
                _, cnt_new = q.popleft()
                heapq.heappush(heap, cnt_new)

        return time

