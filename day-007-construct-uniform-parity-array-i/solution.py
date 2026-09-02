from typing import List

class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        # (a - b) % 2 == (a%2) XOR (b%2), so only odd_count matters:
        # odd_count == 0 or >= 2 lets us build an all-even array,
        # and odd_count >= 1 lets us build an all-odd array (keep the
        # odds, subtract one odd from every even). One of the two
        # always holds, so a valid nums2 always exists.
        return True
