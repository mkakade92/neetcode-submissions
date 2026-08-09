class Twitter:

    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count,tweetId])
        self.count+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:

        res = []

        maxHeap = []

        self.follows[userId].add(userId)
        for followee in self.follows[userId]:

            if followee in self.tweets:
                index = len(self.tweets[followee]) - 1
                count,tweetId = self.tweets[followee][index]
                maxHeap.append([count,tweetId,followee,index-1])
        
        heapq.heapify_max(maxHeap)

        while maxHeap and len(res)<10:

            count, tweetId, followee, index = heapq.heappop_max(maxHeap)
            res.append(tweetId)
            if index>=0:
                count,tweetId = self.tweets[followee][index]
                heapq.heappush_max(maxHeap,[count,tweetId,followee,index-1])
        return res


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
