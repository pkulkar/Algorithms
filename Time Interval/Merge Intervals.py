"""
Leetcode
56. Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all
overlapping intervals, and return an array of the non-overlapping intervals that
cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        start_time = intervals[0][0]
        end_time = intervals[0][1]
        start_index = 1
        merged_intervals = list()
        while start_index < len(intervals):
            new_start = intervals[start_index][0]
            new_end = intervals[start_index][1]
            if new_start <= end_time:
                end_time = max(end_time, new_end)
            else:
                merged_intervals.append([start_time, end_time])
                start_time = new_start
                end_time = new_end
            start_index += 1
        merged_intervals.append([start_time, end_time])
        return merged_intervals
"""
Time Complexity: O(n log n) for sorting where n is number of intervals in the array
Space Complexity: O(n) python sort uses Timsort which has O(n) worst case space complexity
"""
