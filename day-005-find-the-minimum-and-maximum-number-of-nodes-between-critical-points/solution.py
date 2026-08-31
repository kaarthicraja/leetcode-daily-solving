from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        idx = 1

        first_idx = -1
        prev_idx = -1
        min_dist = float('inf')

        while curr and curr.next:
            nxt = curr.next
            is_max = curr.val > prev.val and curr.val > nxt.val
            is_min = curr.val < prev.val and curr.val < nxt.val

            if is_max or is_min:
                if first_idx == -1:
                    first_idx = idx
                    prev_idx = idx
                else:
                    min_dist = min(min_dist, idx - prev_idx)
                    prev_idx = idx

            prev = curr
            curr = curr.next
            idx += 1

        if prev_idx == first_idx:
            return [-1, -1]

        max_dist = prev_idx - first_idx
        return [min_dist, max_dist]
