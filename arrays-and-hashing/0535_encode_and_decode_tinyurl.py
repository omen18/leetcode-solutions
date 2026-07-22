"""
Problem: Encode and Decode TinyURL
LeetCode #: 535
Difficulty: Medium
Link: https://leetcode.com/problems/encode-and-decode-tinyurl/

Approach: Hash map mapping generated short key to long URL using counter or random string generation.
Time Complexity: O(1) average for encode and decode operations.
Space Complexity: O(N) where N is the number of stored URLs.
"""

import random
import string


class Codec:

    def __init__(self):
        self.code_to_url = {}
        self.url_to_code = {}
        self.alphabet = string.ascii_letters + string.digits
        self.base_url = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        if longUrl in self.url_to_code:
            return self.base_url + self.url_to_code[longUrl]

        code = "".join(random.choices(self.alphabet, k=6))
        while code in self.code_to_url:
            code = "".join(random.choices(self.alphabet, k=6))

        self.code_to_url[code] = longUrl
        self.url_to_code[longUrl] = code
        return self.base_url + code

    def decode(self, shortUrl: str) -> str:
        code = shortUrl.replace(self.base_url, "")
        return self.code_to_url[code]
