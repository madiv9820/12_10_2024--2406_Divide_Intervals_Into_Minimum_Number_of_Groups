# 2406. Divide Intervals Into Minimum Number of Groups

__Type:__ Medium <br>
__Topics:__ Array, Two Pointers, Greedy, Sorting, Heap (Priority Queue), Prefix Sum <br>
__Companies:__ Adobe, Walmart Labs <br>
__Leetcode Link:__ [Divide Intervals Into Minimum Number of Groups](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description/)
<hr>

You are given a 2D integer array `intervals` where <code>intervals[i] = [left<sub>i</sub>, right<sub>i</sub>]</code> represents the __inclusive__ interval <code>[left<sub>i</sub>, right<sub>i</sub>]</code>.

You have to divide the intervals into one or more __groups__ such that each interval is in __exactly__ one group, and no two intervals that are in the same group __intersect__ each other.

Return _the __minimum__ number of groups you need to make_.

Two intervals __intersect__ if there is at least one common number between them. For example, the intervals `[1, 5]` and `[5, 8]` intersect.
<hr>

### Examples

__Example 1:__ <br>
__Input:__ intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]] <br>
__Output:__ 3 <br>
__Explanation:__ We can divide the intervals into the following groups: <br> - Group 1: [1, 5], [6, 8]. <br> - Group 2: [2, 3], [5, 10]. <br> - Group 3: [1, 10]. <br>
It can be proven that it is not possible to divide the intervals into fewer than 3 groups.

__Example 2:__ <br>
__Input:__ intervals = [[1,3],[5,6],[8,10],[11,13]] <br>
__Output:__ 1 <br>
__Explanation:__ None of the intervals overlap, so we can put all of them in one group.
<hr>

### Constraints:
- <code>1 <= intervals.length <= 10<sup>5</sup></code>
- `intervals[i].length == 2`
- <code>1 <= lefti <= righti <= 10<sup>6</sup></code>
<hr>

### Hints:
- Can you find a different way to describe the question?
- The minimum number of groups we need is equivalent to the maximum number of intervals that overlap at some point. How can you find that?
