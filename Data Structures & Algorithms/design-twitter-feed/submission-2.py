from collections import defaultdict

class Twitter:

    def __init__(self):
        # store tweets_touples as {userId: [tweetId]}
        # store userId as a key and all users that this user is following: {userId: [userId]}
        # get users feed: get userId and Ids of theirs followers [userIds], for 
        # every userId get the all tweets_touples, sort all tweets_touples and return 10 latest

        self.users = defaultdict(set) # { userId: {userId} }
        self.tweets_touples = defaultdict(list) # { userId: [tweetId] }
        self.counter = 0
        
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets_touples[userId].append((self.counter, tweetId))
        self.counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.users[userId]
        # append users own tweets_touples
        followees.add(userId)
        tweets_touples = []
        for followee in followees:
            current_user_tweets = self.tweets_touples[followee]
            for el in current_user_tweets:
                tweets_touples.append(el)
    
        tweets_touples.sort(reverse=True)
        latest_tuples = tweets_touples[:10]
        latest_tweets = [tweet for counter, tweet in latest_tuples]
        return latest_tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId) # this means we store IDs of all users that followerId is following

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)
        
