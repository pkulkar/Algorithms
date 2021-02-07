"""
Leetcode
3. Longest Substring Without Repeating Characters
    Given a string s, find the length of the longest substring without repeating characters.

    Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

    Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

    Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

    Example 4:
    Input: s = ""
    Output: 0

    Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximumLength, windowStart = 0, 0
        memory = {}
        for windowEnd in range(len(s)):
            rightCharacter = s[windowEnd]
            if rightCharacter not in memory:
                memory[rightCharacter] = 0
            memory[rightCharacter] += 1
            while memory[rightCharacter] > 1:
                leftCharacter = s[windowStart]
                memory[leftCharacter] -= 1
                windowStart += 1
            currentLength = windowEnd - windowStart + 1
            maximumLength = max(currentLength, maximumLength)
        return maximumLength