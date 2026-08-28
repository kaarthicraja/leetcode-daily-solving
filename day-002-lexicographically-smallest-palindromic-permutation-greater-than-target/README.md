# Lexicographically Smallest Palindromic Permutation Greater Than Target

Difficulty: Hard
Topic: Two Pointers, String, Enumeration
LeetCode: https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/

## Problem

You are given two strings s and target, each of length n, consisting of lowercase English letters.

Return the lexicographically smallest string that is both a palindromic permutation of s and strictly greater than target. If no such permutation exists, return an empty string.

 

Example 1:

Input: s = "baba", target = "abba"

Output: "baab"

Explanation:

- The palindromic permutations of s (in lexicographical order) are "abba" and "baab".

- The lexicographically smallest permutation that is strictly greater than target is "baab".

Example 2:

Input: s = "baba", target = "bbaa"

Output: ""

Explanation:

- The palindromic permutations of s (in lexicographical order) are "abba" and "baab".

- None of them is lexicographically strictly greater than target. Therefore, the answer is "".

Example 3:

Input: s = "abc", target = "abb"

Output: ""

Explanation:

s has no palindromic permutations. Therefore, the answer is "".

Example 4:

Input: s = "aac", target = "abb"

Output: "aca"

Explanation:

- The only palindromic permutation of s is "aca".

- "aca" is strictly greater than target. Therefore, the answer is "aca".

 

Constraints:

- 1 <= n == s.length == target.length <= 300

- s and target consist of only lowercase English letters.

## Approach

A palindrome of length n is fully determined by its first ceil(n/2) characters: floor(count/2) copies of each letter go in the half, and (if n is odd) the single odd-count letter is forced into the middle — there is no freedom in *which* letters appear, only in *how the half is ordered*. So the problem reduces to: find the lexicographically smallest ordering of a fixed multiset (the half) that, once mirrored (and given the fixed middle letter), yields a palindrome exceeding target. First check if the half exactly equals target's first half — if so the answer is target's own palindrome-completion when the middle/second-half comparison favors it. Otherwise use a 'next greater permutation with a target multiset' greedy: try to match target's first half as long as possible, then at the latest feasible position place the smallest available character strictly greater than target's, and fill the remainder in ascending order.

**Brute-force alternative:** Generate every distinct palindromic permutation of s (only the first half's arrangement matters since the second half must mirror it), sort them, and linearly/binary-search for the smallest one exceeding target. The number of distinct half-arrangements can be combinatorially huge (up to ~150! / repeats), so this is completely infeasible for n up to 300.

## Algorithm

1. Count letters of s; check parity condition (0 odd counts if n even, exactly 1 if n odd); if violated, no palindrome permutation exists, return "".
2. Build the half-multiset M: for each letter, take count//2 copies (these sum to h = n//2); if n is odd, the leftover odd-count letter becomes the fixed middle character m.
3. Split target into T1 = target[:h], Tm = target[h] (if n odd), T2 = target[h + (n%2):].
4. Equality check: if T1's multiset exactly equals M, the palindrome built directly from T1 is a candidate — accept it if (n odd and m > Tm) or (n odd and m == Tm and reverse(T1) > T2) or (n even and reverse(T1) > T2); if accepted, return T1 + m? + reverse(T1) immediately since matching target exactly as long as possible always gives the smallest valid result.
5. Otherwise (or if the equality candidate fails the condition), search for the smallest half-arrangement A strictly greater than T1: scan candidate match-length i from h-1 down to 0, checking whether T1[:i]'s letter counts fit within M.
6. For the first (largest) feasible i, take the leftover multiset after removing T1[:i]'s letters, find the smallest leftover letter strictly greater than T1[i], place it at position i, then append all remaining leftover letters sorted ascending — this is the smallest valid A for that i, and since i is maximal it's globally smallest.
7. If no such i works (down to i = 0), no arrangement of the half can exceed target, return "".
8. Otherwise return A + m? + reverse(A) as the final palindrome.

## Complexity

Time: O(n * 26)
Space: O(n)

## Edge Cases

- s cannot form any palindrome (more odd-count letters than parity allows) — return ""
- n = 1 (h = 0, only the middle character exists)
- target equals the exact lexicographically smallest palindrome minus one — falls through equality check into the greedy search
- target's first half is not even a permutation of the half-multiset — equality branch skipped entirely
- no arrangement of the half-multiset exceeds target at any split position — return ""
- the only palindromic permutation of s is unique and must be compared directly against target

## Tests

12/12 passed

## Key Learning

A palindrome is fully determined by its first half plus an optional fixed middle character, collapsing the search space from full permutations to half-length arrangements; Splitting a full-string lexicographic comparison into first-half / middle / second-half comparisons lets you reason about each part independently; The 'smallest permutation of a multiset strictly greater than a target string' pattern: match the longest feasible prefix, bump the first divergent position with the smallest larger available character, then fill the rest ascending; Preferring the largest feasible prefix match yields the global optimum because a longer matching prefix always beats any earlier divergence lexicographically

## Review

Score: 8.3/10

Strengths:
- Correctly reduces palindrome construction to ordering a fixed half-multiset, with odd-count check handling infeasibility upfront
- Handles the 'target's half exactly matches multiset' tie case separately and correctly (middle char, then mirrored-second-half comparison)
- Core greedy (scan divergence point from rightmost to leftmost, pick smallest feasible char strictly greater than target's, fill remainder ascending) is the correct algorithm for 'smallest string > target from a fixed multiset', and it's implemented correctly
- Precomputed prefix_counts avoids recomputing Counter(T1[:i]) from scratch each iteration
- Falls through cleanly between the exact-match branch and the general search branch without leaving stale state

Weaknesses:
- Stated time complexity O(n*26) is inaccurate: the final `sorted(remaining.elements())` expands the multiset into up to O(n) individual elements and sorts them, costing O(n log n) on the success path, not O(26 log 26)
- No comments in the code itself explaining the greedy divergence-point logic or the exact-match tie-break; for a Hard problem this subtlety is not self-evident from variable names alone
- Implicitly assumes len(target) == len(s) with no guard, though this is likely a given problem constraint

**A possibly better approach:** Replace `''.join(sorted(remaining.elements()))` with `''.join(c * v for c, v in sorted(remaining.items()))`, which sorts only the ≤26 distinct keys instead of expanding and sorting up to O(n) characters — this actually achieves the claimed O(n + 26 log 26) bound instead of O(n log n).

Key takeaway: A palindrome permutation problem collapses to 'find the smallest multiset-ordering greater than a target prefix', solvable by scanning divergence points from the rightmost position leftward and greedily picking the smallest feasible larger character.

---

*Generated by DSA Daily Agent. This solution was prepared automatically; submitting it on LeetCode is always a manual step.*
