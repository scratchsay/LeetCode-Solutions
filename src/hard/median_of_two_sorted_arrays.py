"""
Runtime: 78 ms (95.11%)
Memory: 17.5 MB (11.42%)
"""

import statistics
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return statistics.median(nums1 + nums2)