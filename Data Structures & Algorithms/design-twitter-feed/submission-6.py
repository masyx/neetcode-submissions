from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed_heap = [] # store 10 most recent tweets
        following = self.following[userId].copy()
        following.add(userId)

        for user in following:
            users_tweets = self.tweets[user]

            for time, tweetId in users_tweets:
                if len(feed_heap) < 10:
                    heapq.heappush(feed_heap, (time, tweetId))
                else:
                    latest_tweet = feed_heap[0][0]
                    if time > latest_tweet:
                        heapq.heappushpop(feed_heap, (time, tweetId))
        feed_heap.sort(reverse=True)
        return [tweetId for time, tweetId in feed_heap]
                
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
