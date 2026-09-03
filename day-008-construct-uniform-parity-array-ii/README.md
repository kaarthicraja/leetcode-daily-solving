# Construct Uniform Parity Array II

Difficulty: Medium
Topic: Array, Math
LeetCode: https://leetcode.com/problems/construct-uniform-parity-array-ii/

## Problem

You are given an array nums1 of n distinct integers.

You want to construct another array nums2 of length n such that the elements in nums2 are either all odd or all even.

For each index i, you must choose exactly one of the following (in any order):

- nums2[i] = nums1[i]​​​​​​​

- nums2[i] = nums1[i] - nums1[j], for an index j != i, such that nums1[i] - nums1[j] >= 1

Return true if it is possible to construct such an array, otherwise return false.

 

Example 1:

Input: nums1 = [1,4,7]

Output: true

Explanation:​​​​​​​​​​​​​​

- Set nums2[0] = nums1[0] = 1.

- Set nums2[1] = nums1[1] - nums1[0] = 4 - 1 = 3.

- Set nums2[2] = nums1[2] = 7.

- nums2 = [1, 3, 7], and all elements are odd. Thus, the answer is true.

Example 2:

Input: nums1 = [2,3]

Output: false

Explanation:

It is not possible to construct nums2 such that all elements have the same parity. Thus, the answer is false.

Example 3:

Input: nums1 = [4,6]

Output: true

Explanation:

- Set nums2[0] = nums1[0] = 4.

- Set nums2[1] = nums1[1] = 6.

- nums2 = [4, 6], and all elements are even. Thus, the answer is true.

 

Constraints:

- 1 <= n == nums1.length <= 105

- 1 <= nums1[i] <= 109

- nums1 consists of distinct integers.

## Approach

Reduce the problem to parity/min-value facts about nums1. Getting an even result from subtraction requires two operands of the same parity (odd-odd=even), and getting an odd result requires operands of opposite parity (even-odd=odd). This means: (1) targeting all-even is only possible if nums1 has no odd numbers at all, because the smallest odd value could never find a smaller odd partner; (2) targeting all-odd is possible if nums1 has no even numbers, or if the global minimum of nums1 is odd (since that odd minimum is then smaller than every even value and can serve as the subtractor for all of them). Compute these two boolean conditions in one linear pass and OR them.

**Brute-force alternative:** For each of the two target parities, and for each index i whose nums1[i] doesn't already match, search all other indices j for one with the required parity and nums1[j] < nums1[i]. This is O(n^2) and unnecessary once you notice the search only cares about the minimum element of the required parity.

## Algorithm

1. Scan nums1 once to check whether it contains any odd values and any even values.
2. If all values already share one parity, return True immediately (no subtraction needed).
3. Otherwise both parities are present: the all-even target is impossible (the smallest odd number has no smaller odd partner).
4. The all-odd target works iff the global minimum of nums1 is odd, since that minimum odd value is smaller than every even value and can be subtracted from each of them to produce an odd result.
5. Return True if the minimum is odd, otherwise False.

## Complexity

Time: O(n)
Space: O(1)

## Edge Cases

- n = 1: array is trivially uniform parity (single element used as-is).
- All elements already odd or already even: answer is True without needing any subtraction.
- Mixed parities where the minimum element is even: answer is False, since neither target parity can be satisfied.
- Mixed parities where the minimum element is odd: answer is True via the all-odd construction.

## Tests

10/10 passed

## Key Learning

Parity of a-b depends only on the parities of a and b (same parity -> even, different parity -> odd), so many array-construction problems collapse to counting/min-value facts rather than needing real search.; When a condition must hold for 'the smallest qualifying element', check whether that specific element can ever satisfy the condition itself — it's often the binding constraint (bottleneck) for the whole array.; Splitting an 'either A or B' feasibility problem into two independent single-condition checks (try all-even, try all-odd) simplifies reasoning versus tracking both simultaneously.

## Review

Score: 6.5/10

Strengths:
- Reduces the problem to a clean O(n) parity/min-value argument instead of any brute-force pairing search
- Correctly short-circuits the trivial case where nums1 is already single-parity
- Passes all 10 provided tests

Weaknesses:
- `from collections import Counter` is imported but never used — dead import
- The `len(nums1) != len(set(nums1))` early return is not derivable from the stated reasoning (parity + global minimum). Per the explained logic, a mixed-parity array with an odd global minimum should return True regardless of duplicates, but this line returns False for e.g. nums1 = [2, 2, 3] before the min-parity check even runs — looks like an unjustified special case, possibly a leftover patch for a failing test rather than a real requirement
- The approach description says the two conditions are computed 'in one linear pass', but the code does four separate O(n) scans (`any`, `any`, `set(...)`, `min(...)`); doesn't change big-O but the description overstates the implementation

**A possibly better approach:** Fold has_odd/has_even/odd-minimum tracking into a single loop with running booleans and a running min, and re-derive (or remove) the duplicate-check branch from the actual problem constraints rather than leaving it unexplained

Key takeaway: A branch that can't be justified from your own stated reasoning is a red flag worth re-verifying against the problem statement, even if it happens to pass the tests you have.

---

*Generated by DSA Daily Agent. This solution was prepared automatically; submitting it on LeetCode is always a manual step.*
