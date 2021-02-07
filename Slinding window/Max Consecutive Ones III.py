"""
Leetcode
1004. Max Consecutive Ones III
    Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
    Return the length of the longest (contiguous) subarray that contains only 1s.
    Example 1:
    Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
    Output: 6
    Explanation:
    [1,1,1,0,0,1,1,1,1,1,1]
    Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

    Example 2:
    Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
    Output: 10
    Explanation:
    [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
    Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

    Note:
    1 <= A.length <= 20000
    0 <= K <= A.length
    A[i] is 0 or 1
"""
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        maximumLength, windowStart, onesCount = 0, 0, 0
        for windowEnd in range(len(A)):
            if A[windowEnd] == 1:
                onesCount += 1
            if (windowEnd - windowStart + 1 - onesCount) > K:
                if A[windowStart] == 1:
                    onesCount -= 1
                windowStart += 1
            currentLength = windowEnd - windowStart + 1
            maximumLength = max(maximumLength, currentLength)
        return maximumLength
            
