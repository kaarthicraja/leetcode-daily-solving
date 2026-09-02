# Construct Uniform Parity Array I

Difficulty: Easy
Topic: Array, Math
LeetCode: https://leetcode.com/problems/construct-uniform-parity-array-i/

## Problem

You are given an array nums1 of n distinct integers.

You want to construct another array nums2 of length n such that the elements in nums2 are either all odd or all even.

For each index i, you must choose exactly one of the following (in any order):

- nums2[i] = nums1[i]

- nums2[i] = nums1[i] - nums1[j], for an index j != i

Return true if it is possible to construct such an array, otherwise, return false.

 

Example 1:

Input: nums1 = [2,3]

Output: true

Explanation:

- Choose nums2[0] = nums1[0] - nums1[1] = 2 - 3 = -1.

- Choose nums2[1] = nums1[1] = 3.

- nums2 = [-1, 3], and both elements are odd. Thus, the answer is true​​​​​​​.

Example 2:

Input: nums1 = [4,6]

Output: true

Explanation:​​​​​​​

- Choose nums2[0] = nums1[0] = 4.

- Choose nums2[1] = nums1[1] = 6.

- nums2 = [4, 6], and all elements are even. Thus, the answer is true.

 

Constraints:

- 1 <= n == nums1.length <= 100

- 1 <= nums1[i] <= 100

- nums1 consists of distinct integers.

## Approach

Since (a - b) mod 2 equals (a mod 2) XOR (b mod 2), only the count of odd numbers matters, not which indices they sit at. Count odd_count. Building an all-even array works if odd_count is 0 (nothing to fix) or at least 2 (every odd element can subtract a different odd element to cancel to even). Building an all-odd array works if odd_count is at least 1 (every even element can subtract that one odd element to flip to odd, and odd elements are kept as-is). Checking both possibilities together turns out to cover every value odd_count can take (0, 1, or >=2), which is the key insight: a valid construction always exists.

**Brute-force alternative:** For each of the two target parities (all-even, all-odd), check every index i: if nums1[i] doesn't already have that parity, scan every other index j to see if nums1[i]-nums1[j] does. This is O(n^2) per target and ignores that the parity of nums1[i]-nums1[j] depends only on the parities of nums1[i] and nums1[j], not their actual magnitudes — so pairwise scanning is wasted work.

## Algorithm

1. Count odd_count = number of odd values in nums1.
2. can_make_all_even = (odd_count == 0) or (odd_count >= 2), since a lone odd number has no other odd number to subtract and stay even.
3. can_make_all_odd = (odd_count >= 1), since any even number can subtract that one odd number to become odd, and existing odd numbers need no change.
4. Return can_make_all_even or can_make_all_odd.

## Complexity

Time: O(n)
Space: O(1)

## Edge Cases

- n = 1: single element is trivially already uniform in parity, no subtraction needed.
- odd_count = 0 (all even): keep nums1 as nums2 directly.
- odd_count = 1: all-even fails (no second odd to pair with), but all-odd succeeds by keeping the odd element and subtracting it from every even element.
- odd_count >= 2 or all elements odd: all-even succeeds by pairing distinct odd elements against each other.

## Tests

12/12 passed on the original (buggy) submission, but the suite never included a mixed-parity input (e.g. `[1,2,3]`), which is why it didn't catch the bug below. `return True` is correct for every input satisfying the constraints (n>=1, distinct integers), since odd_count is always 0, 1, or >=2, and every one of those cases is covered by the construction argument.

## Key Learning

Subtraction parity identity: (a - b) mod 2 == (a mod 2) XOR (b mod 2), so only counts of odd/even matter, not actual values or positions.; Reduce a combinatorial construction question to a counting/invariant question to avoid brute-force pairwise search.; Case-splitting over all possible values of a single derived quantity (here, odd_count) can reveal that a problem's answer is a provable constant rather than input-dependent.

## Review

Score: 9/10 (corrected)

Strengths:
- Now actually encodes the write-up's own conclusion: since odd_count is always 0, 1, or >=2, and each case admits a valid construction (all-even for 0 or >=2, all-odd for >=1), the answer is unconditionally True.
- Correct O(n) time (trivial), O(1) space.

Weaknesses:
- None functionally; a from-scratch implementation could still compute odd_count and construct nums2 explicitly for pedagogical value, but it isn't necessary to answer the boolean question asked.

**Bug found and fixed (2026-09-02):** The original submitted code was `return len({x % 2 for x in nums1}) <= 1` — it checked whether nums1 *already* had uniform parity, which is a different question from whether a uniform-parity nums2 could be *constructed* via the allowed subtraction operation. It ignored odd_count entirely and returned False for any mixed-parity input, directly contradicting the write-up's own "a valid construction always exists" conclusion. Fixed to `return True`, matching the proven case analysis.

Key takeaway: A solution passing its tests doesn't confirm it implements the algorithm you reasoned through — verify the code actually encodes your stated logic (here, odd_count and the construction argument), not just a proxy check that happens to agree on the given tests.

---

*Generated by DSA Daily Agent. This solution was prepared automatically; submitting it on LeetCode is always a manual step.*
