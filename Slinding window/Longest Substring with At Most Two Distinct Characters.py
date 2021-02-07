"""
Leetcode
159. Longest Substring with At Most Two Distinct Characters
  Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

  Example 1:

  Input: "eceba"
  Output: 3
  Explanation: t is "ece" which its length is 3.
  Example 2:

  Input: "ccaabbb"
  Output: 5
  Explanation: t is "aabbb" which its length is 5.
"""
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        maximumLength, windowStart = 0, 0
        memory = {}
        for windowEnd in range(len(s)):
            rightCharacter = s[windowEnd]
            if rightCharacter not in memory:
                memory[rightCharacter] = 0
            memory[rightCharacter] += 1
            while len(memory) > 2:
                leftCharacter = s[windowStart]
                memory[leftCharacter] -= 1
                if memory[leftCharacter] == 0:
                    del memory[leftCharacter]
                windowStart += 1
            currentLength = windowEnd - windowStart + 1
            maximumLength = max(maximumLength, currentLength)
        return maximumLength
