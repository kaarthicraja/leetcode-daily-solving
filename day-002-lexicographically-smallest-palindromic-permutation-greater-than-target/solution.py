from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)
        mid_required = n % 2
        odd_chars = [c for c, v in cnt.items() if v % 2 == 1]
        if len(odd_chars) != mid_required:
            return ""

        h = n // 2
        M = Counter({c: v // 2 for c, v in cnt.items() if v // 2 > 0})
        m_char = odd_chars[0] if mid_required else None

        T1 = target[:h]
        Tm = target[h] if mid_required else None
        T2 = target[h + mid_required:]

        if Counter(T1) == M:
            ok = False
            if mid_required:
                if m_char > Tm:
                    ok = True
                elif m_char == Tm and T1[::-1] > T2:
                    ok = True
            else:
                if T1[::-1] > T2:
                    ok = True
            if ok:
                return T1 + (m_char if mid_required else "") + T1[::-1]

        prefix_counts = [Counter()]
        for ch in T1:
            nxt = prefix_counts[-1].copy()
            nxt[ch] += 1
            prefix_counts.append(nxt)

        for i in range(h - 1, -1, -1):
            pc = prefix_counts[i]
            if any(pc[c] > M.get(c, 0) for c in pc):
                continue

            remaining = M.copy()
            for c, v in pc.items():
                remaining[c] -= v
                if remaining[c] <= 0:
                    del remaining[c]

            target_char = T1[i]
            greater = sorted(c for c in remaining if c > target_char)
            if not greater:
                continue

            chosen = greater[0]
            remaining[chosen] -= 1
            if remaining[chosen] == 0:
                del remaining[chosen]

            rest = ''.join(sorted(remaining.elements()))
            A = T1[:i] + chosen + rest
            return A + (m_char if mid_required else "") + A[::-1]

        return ""
