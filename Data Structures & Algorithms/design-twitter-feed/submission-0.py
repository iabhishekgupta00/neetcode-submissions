import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {}      # userId -> [(time, tweetId)]
        self.following = {}   # userId -> set of followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        # User's own tweets
        users = {userId}

        # People user follows
        users.update(self.following.get(userId, set()))

        # Put tweets into heap
        for user in users:
            if user in self.tweets:
                for time, tweetId in self.tweets[user][-10:]:
                    heapq.heappush(heap, (time, tweetId))

                    if len(heap) > 10:
                        heapq.heappop(heap)

        # Newest first
        result = []

        while heap:
            time, tweetId = heapq.heappop(heap)
            result.append(tweetId)

        return result[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)