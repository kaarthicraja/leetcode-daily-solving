from typing import List

class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        parities = {x % 2 for x in nums1}
        return len(parities) <= 1
