"""
Leetcode
643. Maximum Average Subarray I
    Given an array consisting of n integers, find the contiguous subarray
    of given length k that has the maximum average value. And you need to
    output the maximum average value.

        Example 1:

        Input: [1,12,-5,-6,50,3], k = 4
        Output: 12.75
        Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75


        Note:

        1 <= k <= n <= 30,000.
        Elements of the given array will be in the range [-10,000, 10,000].
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        addition, windowStart = 0.0, 0
        maxAverage = float('-inf')
        for windowEnd in range(len(nums)):
            addition += nums[windowEnd]
            if windowEnd >= k-1:
                average = addition / k
                maxAverage = max(maxAverage, average)
                addition -= nums[windowStart]
                windowStart += 1
        return maxAverage
