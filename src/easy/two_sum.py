"""
Runtime: 51 ms (98.36%)
Memory 18.7 MB (6.9%)
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_map = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_index_map:
                return [num_index_map[complement], i]
            num_index_map[num] = i

        return []

# Run code
print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([3, 2, 4], 6))
print(Solution().twoSum([3, 3], 6))
