class Twitter:

    def __init__(self)->None:
        # key is who is follower (person doing the following)
        # value is list of followees (people being followered)
        self.followers: dict[int, set[int]] = {}
        # WARNING: Below was a failed though process, ignore it
        # tweets of users should be stored here
        # key is user id, can be used in followers dict
        # For every user created, an empty list is intialised.
        # This should be a max heap of max 10 values and based on who
        # follows who
        # WARNING: Above was a failed though process, ignore it.
        # This has to be extracted live from whoever the person is following.
        # We store key as user_id and a max_heap of posts that user has posted
        # based on time. So when get news feed is called, we get latest of
        # each followed user.
        # That tuple is (time, tweet_id)
        self.tweets: dict[int, list[tuple[int, int]]] = {}

        # This will get incremented everytime a tweet is posted
        # used for the max heap storage, not using datetime since
        # its a mock twitter.
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        if not userId in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.time,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        We have each followed persons max_heap of tweets
        including his own.
        We maintain a feed_max_heap where we first people
        a value from all followed users including themselves and put in feed_max_heap.
        Then we pop 1 value from feed_max_heap and then add value from all the other max_heaps again.
        We iterate this till either result has 10 values or till
        no more tweets are left
        """
        if userId not in self.followers:
            followees = set()
        else:
            followees = self.followers[userId].copy()

        followees.add(userId)
        feed_max_heap = []
        res = []
        # insert first of each followee
        for followee in followees:
            if followee in self.tweets and 0<len(self.tweets[followee]):
                index = len(self.tweets[followee]) - 1
                time, tweetId = self.tweets[followee][index]
                heapq.heappush(feed_max_heap, (-time, tweetId, followee, index))

        feed = []
        while len(feed)<10 and feed_max_heap:
            neg_time, tweetId, followee, index = heapq.heappop(feed_max_heap)
            feed.append(tweetId)
            index -=1
            if index >= 0:
                time, tweetId = self.tweets[followee][index]
                heapq.heappush(feed_max_heap, (-time, tweetId, followee, index))
        return feed
            
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        
