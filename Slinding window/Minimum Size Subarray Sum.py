"""
Leetcode
209. Minimum Size Subarray Sum

    Given an array of positive integers nums and a positive integer target, return the minimal length
    of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than
    or equal to target. If there is no such subarray, return 0 instead.

        Example 1:

        Input: target = 7, nums = [2,3,1,2,4,3]
        Output: 2
        Explanation: The subarray [4,3] has the minimal length under the problem constraint.
        Example 2:

        Input: target = 4, nums = [1,4,4]
        Output: 1
        Example 3:

        Input: target = 11, nums = [1,1,1,1,1,1,1,1]
        Output: 0


        Constraints:

        1 <= target <= 109
        1 <= nums.length <= 105
        1 <= nums[i] <= 105

"""
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        windowSum, windowStart = 0, 0
        minimumLength = float('inf')
        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]
            while windowSum >= s:
                length = windowEnd - windowStart + 1
                minimumLength = min(length, minimumLength)
                windowSum -= nums[windowStart]
                windowStart += 1
        if minimumLength == float('inf'):
            return 0
        return minimumLength
