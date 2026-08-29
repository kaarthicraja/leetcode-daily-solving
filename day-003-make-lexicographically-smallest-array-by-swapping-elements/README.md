# Make Lexicographically Smallest Array by Swapping Elements

Difficulty: Medium
Topic: Array, Union-Find, Sorting
LeetCode: https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/

## Problem

You are given a 0-indexed array of positive integers nums and a positive integer limit.

In one operation, you can choose any two indices i and j and swap nums[i] and nums[j] if |nums[i] - nums[j]| <= limit.

Return the lexicographically smallest array that can be obtained by performing the operation any number of times.

An array a is lexicographically smaller than an array b if in the first position where a and b differ, array a has an element that is less than the corresponding element in b. For example, the array [2,10,3] is lexicographically smaller than the array [10,2,3] because they differ at index 0 and 2 < 10.

 

Example 1:

Input: nums = [1,5,3,9,8], limit = 2
Output: [1,3,5,8,9]
Explanation: Apply the operation 2 times:
- Swap nums[1] with nums[2]. The array becomes [1,3,5,9,8]
- Swap nums[3] with nums[4]. The array becomes [1,3,5,8,9]
We cannot obtain a lexicographically smaller array by applying any more operations.
Note that it may be possible to get the same result by doing different operations.

Example 2:

Input: nums = [1,7,6,18,2,1], limit = 3
Output: [1,6,7,18,1,2]
Explanation: Apply the operation 3 times:
- Swap nums[1] with nums[2]. The array becomes [1,6,7,18,2,1]
- Swap nums[0] with nums[4]. The array becomes [2,6,7,18,1,1]
- Swap nums[0] with nums[5]. The array becomes [1,6,7,18,1,2]
We cannot obtain a lexicographically smaller array by applying any more operations.

Example 3:

Input: nums = [1,7,28,19,10], limit = 3
Output: [1,7,28,19,10]
Explanation: [1,7,28,19,10] is the lexicographically smallest array we can obtain because we cannot apply the operation on any two indices.

 

Constraints:

- 1 <= nums.length <= 105

- 1 <= nums[i] <= 109

- 1 <= limit <= 109

## Approach

Sort the array's (value, index) pairs by value. Since indices are processed in increasing value order, any two consecutive values whose difference exceeds limit break the chain into a new connected component (union-find style grouping via sorted adjacency, which is equivalent to actual union-find but simpler here because sorted order guarantees the closest candidates are adjacent). Within each component, the original indices are sorted and the already-sorted values are placed into those indices in order — this yields the lexicographically smallest arrangement for that group.

**Brute-force alternative:** Simulate swaps directly or repeatedly try swapping any pair whose difference is within limit until no more improving swaps exist; this is exponential/very slow since it doesn't recognize the transitive connectivity, and doesn't scale to n = 10^5.

## Algorithm

1. Pair each value with its original index and sort pairs by value.
2. Walk through the sorted pairs, starting a new group whenever the difference between the current value and the previous value exceeds limit (this defines connected components, since within a sorted run all consecutive gaps are <= limit meaning every value can reach its neighbor).
3. For each completed group, take the collected original indices and sort them ascending.
4. Assign the group's values (already in sorted order from step 1) to the sorted indices in order, smallest value to smallest index.
5. After processing all groups, return the result array.

## Complexity

Time: O(n log n)
Space: O(n)

## Edge Cases

- Single-element array: no swaps possible, returns nums unchanged.
- No two elements within limit of each other: every element is its own group, array is returned as-is (matches Example 3).
- All elements within limit of each other: whole array becomes one group and is fully sorted.
- Duplicate values: difference of 0 is always <= limit (limit >= 1), so duplicates always merge into the same group correctly.
- Very large limit (e.g. 10^9) or large value range: handled fine since only differences are compared, no overflow issues in Python.

## Tests

10/10 passed

## Key Learning

Recognizing when a swap relation defines connected components (union-find pattern) even without explicitly building a union-find structure, by exploiting sorted order.; Within any connected component, elements can be freely permuted, so the lexicographically smallest result places sorted values at sorted original index positions.; Sorting by value first turns a graph-connectivity problem into a simple linear scan for adjacency-based grouping.; Separating 'value order' from 'index order' and recombining them is a common technique for problems requiring conditional rearrangement.

## Review

Score: 8.7/10

Strengths:
- Correctly reduces the problem to connected components using sorted-adjacency instead of a full union-find, which is a nice simplification since sorted order guarantees the tightest gaps are between neighbors
- Within-group greedy (sorted indices get sorted values) is proven optimal for lexicographic minimality
- Achieves O(n log n) time / O(n) space, which is asymptotically optimal for this problem
- Clean separation of grouping logic and placement logic via flush_group

Weaknesses:
- flush_group reads group_indices/group_values from the enclosing scope but the caller resets those same names right after calling it — works correctly but relies on non-obvious closure semantics rather than the function owning its own reset, which could confuse a reader or break if someone reassigns instead of appending to those lists later

Key takeaway: When elements are processed in sorted order, connectivity for an 'edge if difference <= limit' graph can be tracked with a simple sequential adjacency check instead of full union-find, since sorted order guarantees the smallest possible gap is always between consecutive elements.

---

*Generated by DSA Daily Agent. This solution was prepared automatically; submitting it on LeetCode is always a manual step.*
