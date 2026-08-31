# Find the Minimum and Maximum Number of Nodes Between Critical Points

Difficulty: Medium
Topic: Linked List
LeetCode: https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

## Problem

A critical point in a linked list is defined as either a local maxima or a local minima.

A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].

 

Example 1:

Input: head = [3,1]
Output: [-1,-1]
Explanation: There are no critical points in [3,1].

Example 2:

Input: head = [5,3,1,2,5,1,2]
Output: [1,3]
Explanation: There are three critical points:
- [5,3,1,2,5,1,2]: The third node is a local minima because 1 is less than 3 and 2.
- [5,3,1,2,5,1,2]: The fifth node is a local maxima because 5 is greater than 2 and 1.
- [5,3,1,2,5,1,2]: The sixth node is a local minima because 1 is less than 5 and 2.
The minimum distance is between the fifth and the sixth node. minDistance = 6 - 5 = 1.
The maximum distance is between the third and the sixth node. maxDistance = 6 - 3 = 3.

Example 3:

Input: head = [1,3,2,2,3,2,2,2,7]
Output: [3,3]
Explanation: There are two critical points:
- [1,3,2,2,3,2,2,2,7]: The second node is a local maxima because 3 is greater than 1 and 2.
- [1,3,2,2,3,2,2,2,7]: The fifth node is a local maxima because 3 is greater than 2 and 2.
Both the minimum and maximum distances are between the second and the fifth node.
Thus, minDistance and maxDistance is 5 - 2 = 3.
Note that the last node is not considered a local maxima because it does not have a next node.

 

Constraints:

- The number of nodes in the list is in the range [2, 105].

- 1 <= Node.val <= 105

## Approach

Traverse the list once with three pointers (prev, curr, next) tracking position. Whenever curr is a critical point, record its index. Keep track of the first critical index and the previous critical index seen so far: update maxDistance as (current index - first index), and update minDistance as the minimum of (current index - previous critical index) seen consecutively, since critical points alternate and consecutive critical points always give the smallest possible gaps.

**Brute-force alternative:** Traverse the list once to collect the index of every critical point into a list, then do a nested loop comparing every pair of indices to find the min and max difference — this works but is O(k^2) for k critical points when a single linear pass over the sorted-by-position indices already gives the answer.

## Algorithm

1. Move a pointer through the list keeping references to previous, current, and next node values along with current's 0-based index.
2. For each current node that has both a previous and next neighbor, check if it is strictly greater than both (local maxima) or strictly less than both (local minima) — if so it's a critical point.
3. If it's the first critical point found, store its index as firstIdx and also as prevIdx (previous critical point index).
4. Otherwise, compute distance = currentIdx - prevIdx, update minDistance = min(minDistance, distance), update maxDistance = currentIdx - firstIdx, and set prevIdx = currentIdx.
5. After traversal, if fewer than two critical points were found, return [-1, -1], otherwise return [minDistance, maxDistance].

## Complexity

Time: O(n)
Space: O(1)

## Edge Cases

- Fewer than 2 nodes or no critical points at all -> returns [-1, -1]
- Exactly one critical point found -> still returns [-1, -1] since prev_idx equals first_idx
- Critical points at the very first or last node are correctly excluded since they lack a neighbor on one side
- Plateaus (equal adjacent values) are correctly not counted since the comparisons are strict
- Two consecutive critical points give the minimum possible distance of 1

## Tests

Not automatically tested — this problem's input/output shape (linked list, tree, or in-place mutation) isn't yet supported by the execution harness. Please verify manually before submitting.

## Key Learning

Single-pass linked list traversal with a sliding window of prev/curr/next pointers; Tracking running aggregates (first, previous, min, max) instead of storing all indices avoids extra space and a second pass; Recognizing that only consecutive critical points need to be compared for the minimum distance, since any non-consecutive pair's gap is strictly larger; Strict inequality comparisons to correctly define local maxima/minima and exclude plateaus

## Review

Score: 9.5/10

Strengths:
- Correct single-pass O(n) time, O(1) space solution
- Correctly limits min-distance tracking to consecutive critical points only, which is the key insight for optimality
- Critical point condition (strict inequality on both neighbors) correctly implemented, so plateaus/ties are properly excluded
- Clean early return of [-1, -1] when fewer than two critical points exist

Weaknesses:
- Assumes head and head.next are non-None without guarding; relies implicitly on LeetCode's n>=2 constraint rather than being defensive

Key takeaway: For minimum distance between critical points, only comparing consecutive critical points is needed since any non-adjacent pair's gap is necessarily larger.

---

*Generated by DSA Daily Agent. This solution was prepared automatically; submitting it on LeetCode is always a manual step.*
