"""
Runtime: 41 ms (93.59%)
Memory 17.4 MB (5.6%)
"""

from typing import List


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            total_sum = l1_val + l2_val + carry
            carry, remainder = divmod(total_sum, 10)

            curr.next = ListNode(remainder)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
