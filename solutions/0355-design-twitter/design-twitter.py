class Twitter:

    def __init__(self):
        self.follow_map = collections.defaultdict(set)
        self.tweet_map = collections.defaultdict(list)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweet_map[userId].append((-self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        # go thru all following
        # maintain a heap of (timestamp, tweetid) from each follower including self
        heap = []
        res = []
        for follower in self.follow_map[userId]:
            if self.tweet_map[follower]:
                timestamp, tweetId = self.tweet_map[follower][-1]
                heapq.heappush(heap, (timestamp, follower, -1, tweetId))
        if self.tweet_map[userId]:
            timestamp, tweetId = self.tweet_map[userId][-1]
            heapq.heappush(heap, (timestamp, userId, -1, tweetId))
        while len(res) != 10 and heap:
            _, follower, number, tweetId = heapq.heappop(heap)
            # res.insert(0, tweetId)
            res.append(tweetId)
            if len(self.tweet_map[follower]) >= -(number-1):
                ts, twtId = self.tweet_map[follower][number-1]
                heapq.heappush(heap, (ts, follower, number-1, twtId))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
