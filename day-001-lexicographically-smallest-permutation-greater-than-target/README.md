# Lexicographically Smallest Permutation Greater Than Target

Difficulty: Medium
Topic: Hash Table, String, Greedy, Counting, Enumeration
LeetCode: https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/

## Problem

You are given two strings s and target, both having length n, consisting of lowercase English letters.

Return the lexicographically smallest permutation of s that is strictly greater than target. If no permutation of s is lexicographically strictly greater than target, return an empty string.

A string a is lexicographically strictly greater than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b.

 

Example 1:

Input: s = "abc", target = "bba"

Output: "bca"

Explanation:

- The permutations of s (in lexicographical order) are "abc", "acb", "bac", "bca", "cab", and "cba".

- The lexicographically smallest permutation that is strictly greater than target is "bca".

Example 2:

Input: s = "leet", target = "code"

Output: "eelt"

Explanation:

- The permutations of s (in lexicographical order) are "eelt", "eetl", "elet", "elte", "etel", "etle", "leet", "lete", "ltee", "teel", "tele", and "tlee".

- The lexicographically smallest permutation that is strictly greater than target is "eelt".

Example 3:

Input: s = "baba", target = "bbaa"

Output: ""

Explanation:

- The permutations of s (in lexicographical order) are "aabb", "abab", "abba", "baab", "baba", and "bbaa".

- None of them is lexicographically strictly greater than target. Therefore, the answer is "".

 

Constraints:

- 1 <= s.length == target.length <= 300

- s and target consist of only lowercase English letters.

## Approach

Greedily decide the answer digit by digit like in 'next greater number' problems, but with a fixed multiset of letters instead of free digit choice. First find the longest prefix length L for which target's prefix can actually be built from s's letter counts. Then, starting from the deepest feasible deviation point (i = min(L, n-1)) and working backwards toward index 0, try to copy target exactly up to position i, then at position i place the smallest available letter that is strictly greater than target[i], and fill every remaining position with the leftover letters in ascending order (which is always the smallest possible suffix). The first (i.e., deepest) position where such a greater letter exists gives the lexicographically smallest valid answer, because matching target for as long as possible before deviating keeps the result as close to target as possible.

**Brute-force alternative:** Generate every permutation of s, sort them, and scan for the first one greater than target. This is O(n!) time and completely infeasible once n grows past ~10, let alone n = 300.

## Algorithm

1. Build a frequency count 'base' of all letters in s.
2. Simulate consuming target's letters from a copy of base to find L, the longest prefix of target that is a sub-multiset of s (stop at the first letter that runs out).
3. Set i_max = min(L, n-1); this is the deepest index we could possibly deviate at while still matching target before it.
4. Maintain 'used' = frequency count of target[:i] as i decreases from i_max to 0.
5. For each i from i_max down to 0: compute remaining = base - used (letters still available after reserving target[:i]).
6. Search remaining for the smallest letter strictly greater than target[i]; if found, place it at position i, then append all leftover letters in ascending order as the suffix, and return target[:i] + that letter + suffix.
7. If no such letter exists at this i, shrink the matched prefix by giving back target[i-1] into 'used' minus one, and try i-1.
8. If no i (including i = 0) works, return an empty string.

## Complexity

Time: O(n) (each of the n candidate deviation positions does O(26) work for the alphabet-sized counters, so effectively O(26n))
Space: O(n) for the output string and the used/remaining counters (bounded by 26 keys)

## Edge Cases

- s is already the lexicographically largest permutation (e.g. s='cba', target='cba') → returns ''
- n = 1 with s == target → no strictly greater single-letter permutation → returns ''
- target's prefix cannot be matched at all by s (L = 0) → deviation must happen at index 0
- s can match target exactly for its full length (L = n) → deviation point is capped at n-1
- Duplicate letters in s requiring correct multiset bookkeeping instead of treating letters as unique
- target itself is not required to be a permutation of s's letters

## Tests

10/10 passed

## Key Learning

Greedy 'match prefix as long as possible, then bump the first divergent digit with the smallest larger option, then fill smallest suffix' pattern (same idea as next-permutation / smallest-number-greater-than-x problems); Working backwards from the deepest feasible deviation point yields the lexicographically closest (hence smallest) valid answer; Using frequency counters (multisets) instead of treating characters as distinguishable, since s can contain duplicate letters; Precomputing the longest matchable prefix avoids wasted work trying deviation points that are provably infeasible

## Review

Score: 8.5/10

Strengths:
- Correctly bounds the search using the longest feasible prefix L, handling the tricky edge case where target's own prefix isn't buildable from s's letters (verified this doesn't break the used/remaining invariant since any prefix of a feasible prefix is itself feasible)
- Adapts the classic 'next greater permutation' backward-greedy pattern cleanly to a fixed multiset instead of free digit choice
- O(26n) via Counter arithmetic avoids brute-force permutation generation, and the stated complexity is accurate
- Ascending fill of leftover letters for the suffix correctly guarantees the smallest possible tail once a deviation point is chosen

Weaknesses:
- No comment explaining why i_max = min(L, n-1) is safe even though target[:L+1] itself may be infeasible — this is the least obvious part of the algorithm and would benefit from a short note
- remaining = base - used is recomputed from scratch via Counter subtraction on every outer-loop iteration instead of being updated incrementally, adding avoidable constant-factor work
- Hardcodes ord('z') as the alphabet ceiling, silently assuming lowercase a-z input with no validation
- Terse names like L and i_max require re-deriving their meaning from the loop body rather than the name itself

Key takeaway: When porting 'next greater' greedy logic to a fixed multiset, first compute the longest prefix of target actually buildable from that multiset — deviating anywhere beyond it is invalid, and the deviation point itself can legitimately sit right at that boundary even though the full prefix through it isn't achievable.

---

*Generated by DSA Daily Agent. This solution was prepared automatically; submitting it on LeetCode is always a manual step.*
