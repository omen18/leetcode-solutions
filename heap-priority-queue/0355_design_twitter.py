"""
Problem: Design Twitter
LeetCode #: 355
Difficulty: Medium
Link: https://leetcode.com/problems/design-twitter/

Approach: Use a global time counter to sequence tweets.
Maintain a mapping of userId to list of their tweets (count, tweetId), and a mapping of followerId to set of followees.
To get news feed for a user, collect the latest tweets from the user and all followees, use a max-heap (or min-heap of top 10) to retrieve up to 10 most recent tweets.

Time Complexity:
  - postTweet: O(1)
  - getNewsFeed: O(F log F) where F is the number of followees
  - follow: O(1)
  - unfollow: O(1)
Space Complexity: O(U + T) where U is total users and T is total tweets
"""

from collections import defaultdict
import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.count = 0
        self.tweet_map = defaultdict(list)  # userId -> list of (count, tweetId)
        self.follow_map = defaultdict(set)   # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        self.follow_map[userId].add(userId)

        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map:
                index = len(self.tweet_map[followeeId]) - 1
                count, tweetId = self.tweet_map[followeeId][index]
                min_heap.append((count, tweetId, followeeId, index - 1))

        heapq.heapify(min_heap)

        while min_heap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(min_heap)
            res.append(tweetId)
            if index >= 0:
                next_count, next_tweetId = self.tweet_map[followeeId][index]
                heapq.heappush(min_heap, (next_count, next_tweetId, followeeId, index - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
