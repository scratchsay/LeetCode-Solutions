"""
Runtime: 55 ms (81.19%)
Memory 17.4 MB (8.69%)
"""

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, max_length = 0, 0
        last_indexes = {}

        for i, char in enumerate(s):
            if char in last_indexes:
                start = max(last_indexes[char] + 1, start)

            max_length = max(max_length, i - start + 1)
            last_indexes[char] = i

        return max_length
