"""
Runtime: 42 ms (98.6%)
Memory: 17.3 MB (5.42%)
"""

from typing import List


class Solution:
    def is_palindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)

# Run code
print(Solution().is_palindrome(121))
print(Solution().is_palindrome(-121))
print(Solution().is_palindrome(10))
