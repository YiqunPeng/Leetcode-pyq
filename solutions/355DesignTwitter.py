import heapq


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.follow_dict = collections.defaultdict(set)
        self.n = 0
        self.user_tweet = collections.defaultdict(set)
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.user_tweet[userId].add((self.n, tweetId))
        self.n += 1
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        heap = []
        
        candid = self.follow_dict[userId]
        candid.add(userId)
        
        for i in candid:
            for t in self.user_tweet[i]:
                heapq.heappush(heap, t)
                if len(heap) > 10:
                    heapq.heappop(heap)
        
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res[::-1]      
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.follow_dict[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId in self.follow_dict[followerId]:
            self.follow_dict[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)