class Twitter:

    def __init__(self):
        self.followers = defaultdict(set) #followee: follower 
        self.posts = defaultdict(list) #user: tweetID
        self.counter = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.counter, tweetId))
        self.counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for f in self.followers[userId]:
            for t in self.posts[f]:
                heapq.heappush(heap,t)
        for t in self.posts[userId]:
            heapq.heappush(heap,t)
        while len(heap) > 10:
            heapq.heappop(heap)
        ret = []
        while heap:
            timestamp, tweetId = heapq.heappop(heap)
            ret.append(tweetId)
        return ret[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)