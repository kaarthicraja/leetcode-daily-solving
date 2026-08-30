from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        i = nums.index(min(nums))
        j = nums.index(max(nums))
        lo, hi = min(i, j), max(i, j)

        from_front = hi + 1
        from_back = n - lo
        both_ends = (lo + 1) + (n - hi)

        return min(from_front, from_back, both_ends)