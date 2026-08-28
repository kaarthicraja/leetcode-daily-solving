class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = int(''.join(map(str, digits))) + 1
        return [int(d) for d in str(n)]
