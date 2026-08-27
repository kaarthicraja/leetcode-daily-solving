from collections import Counter


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        base = Counter(s)

        temp = Counter(s)
        L = n
        for i in range(n):
            c = target[i]
            if temp[c] > 0:
                temp[c] -= 1
            else:
                L = i
                break

        i_max = min(L, n - 1)
        used = Counter(target[:i_max])

        for i in range(i_max, -1, -1):
            remaining = base - used
            found = None
            for code in range(ord(target[i]) + 1, ord('z') + 1):
                c = chr(code)
                if remaining[c] > 0:
                    found = c
                    break
            if found:
                remaining[found] -= 1
                tail_chars = []
                for code in range(ord('a'), ord('z') + 1):
                    c = chr(code)
                    if remaining[c] > 0:
                        tail_chars.append(c * remaining[c])
                return target[:i] + found + ''.join(tail_chars)
            if i > 0:
                prev = target[i - 1]
                used[prev] -= 1
                if used[prev] == 0:
                    del used[prev]

        return ""
