"""
Runtime: 32 ms (91.5%)
Memory: 17.4 MB (6.62%)
"""
from typing import List

class Solution:
    def min_start_value(self, nums: List[int]) -> int:
        total = 0
        current_min = 0
        for num in nums:
            total += num
            current_min = min(current_min, total)

        return -current_min + 1

# Run code
print(Solution().min_start_value([-3, 2, -3, 4, 2]))
print(Solution().min_start_value([1, 2]))
print(Solution().min_start_value([1, -2, -3]))