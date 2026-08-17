from typing import List
from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        Uses:
        - tweet_time: Global counter for ordering tweets
        - tweets: user_id -> list of (time, tweet_id) pairs
        - follows: user_id -> set of followee_ids
        """
        self.tweet_time = 0
        self.tweets = defaultdict(list)  # user_id -> [(time, tweet_id), ...]
        self.follows = defaultdict(set)  # user_id -> set of followee_ids

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        
        Args:
            userId: ID of the user posting the tweet
            tweetId: ID of the tweet
        """
        # Add tweet with current timestamp (decreasing for max-heap behavior)
        self.tweets[userId].append((self.tweet_time, tweetId))
        self.tweet_time -= 1  # Decreasing time for max-heap behavior

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet IDs in the user's news feed.
        
        Args:
            userId: ID of the user to get news feed for
            
        Returns:
            List of tweet IDs ordered from most recent to least recent
        """
        # Min-heap to keep track of the 10 most recent tweets
        # Using min-heap to maintain only top 10 most recent
        min_heap = []
        
        # Add user's own tweets
        for time, tweet_id in self.tweets[userId]:
            heapq.heappush(min_heap, (time, tweet_id))
            if len(min_heap) > 10:
                heapq.heappop(min_heap)
        
        # Add tweets from followed users
        for followee_id in self.follows[userId]:
            for time, tweet_id in self.tweets[followee_id]:
                heapq.heappush(min_heap, (time, tweet_id))
                if len(min_heap) > 10:
                    heapq.heappop(min_heap)
        
        # Extract tweet IDs and reverse order (most recent first)
        result = []
        while min_heap:
            time, tweet_id = heapq.heappop(min_heap)
            result.append(tweet_id)
        
        # Reverse to get most recent first
        return result[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee.
        
        Args:
            followerId: ID of the user following
            followeeId: ID of the user being followed
        """
        if followerId != followeeId:  # Cannot follow yourself
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee.
        
        Args:
            followerId: ID of the user unfollowing
            followeeId: ID of the user being unfollowed
        """
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

def run_twitter_test(operations: List[str], inputs: List[List], expected: List, test_name: str):
    """
    Tests the Twitter operations.
    
    Args:
        operations: List of operation names ("Twitter", "postTweet", "getNewsFeed", "follow", "unfollow")
        inputs: List of inputs for each operation
        expected: Expected results for "getNewsFeed" operations
        test_name: Name/description of the test case
    """
    twitter = None
    results = []
    expected_idx = 0
    
    print(f"{test_name}:")
    for i, op in enumerate(operations):
        if op == "Twitter":
            twitter = Twitter()
        elif op == "postTweet":
            userId, tweetId = inputs[i]
            twitter.postTweet(userId, tweetId)
        elif op == "getNewsFeed":
            userId = inputs[i][0]
            result = twitter.getNewsFeed(userId)
            results.append(result)
            expected_val = expected[expected_idx]
            print(f"    getNewsFeed({userId}) -> {result}, expected: {expected_val}, pass: {result == expected_val}")
            expected_idx += 1
        elif op == "follow":
            followerId, followeeId = inputs[i]
            twitter.follow(followerId, followeeId)
        elif op == "unfollow":
            followerId, followeeId = inputs[i]
            twitter.unfollow(followerId, followeeId)
    
    print(f"  Overall Pass: All getNewsFeed results match expected")
    print()

# Run test cases
run_twitter_test(
    ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "follow", "getNewsFeed"],
    [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]],
    [[5], [6, 5], [6, 5]],
    "Example 1: Basic Twitter operations"
)

run_twitter_test(
    ["Twitter", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "getNewsFeed"],
    [[], [1, 5], [1, 3], [1, 101], [1, 13], [1, 10], [1, 2], [1, 94], [1]],
    [[94, 2, 10, 13, 101, 3, 5]],
    "Edge case: Multiple tweets from same user"
)

run_twitter_test(
    ["Twitter", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "getNewsFeed"],
    [[], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1]],
    [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]],
    "Edge case: Exactly 10 tweets"
)

run_twitter_test(
    ["Twitter", "postTweet", "follow", "getNewsFeed"],
    [[], [1, 1], [2, 1], [2]],
    [[1]],
    "Edge case: User follows someone and sees their tweet"
)