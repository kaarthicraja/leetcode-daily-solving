from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        order = sorted(range(n), key=lambda i: nums[i])
        result = [0] * n

        group_indices = []
        group_values = []

        def flush_group():
            for idx, val in zip(sorted(group_indices), group_values):
                result[idx] = val

        for k, idx in enumerate(order):
            if k > 0 and nums[idx] - nums[order[k - 1]] > limit:
                flush_group()
                group_indices = []
                group_values = []
            group_indices.append(idx)
            group_values.append(nums[idx])

        if group_indices:
            flush_group()

        return result