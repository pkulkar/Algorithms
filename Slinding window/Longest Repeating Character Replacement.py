"""
Leetcode
424. Longest Repeating Character Replacement
    Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.
    In one operation, you can choose any character of the string and change it to any other uppercase English character.
    Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.
    Note:
    Both the string's length and k will not exceed 104.

    Example 1:
    Input:
    s = "ABAB", k = 2
    Output:
    4
    Explanation:
    Replace the two 'A's with two 'B's or vice versa.

    Example 2:
    Input:
    s = "AABABBA", k = 1
    Output:
    4
    Explanation:
    Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    The substring "BBBB" has the longest repeating letters, which is 4.
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maximumLength, windowStart = 0, 0
        maximumRepeated = 0
        memory = {}
        for windowEnd in range(len(s)):
            rightCharacter = s[windowEnd]
            if rightCharacter not in memory:
                memory[rightCharacter] = 0
            memory[rightCharacter] += 1
            maximumRepeated = max(memory[rightCharacter], maximumRepeated)
            if (windowEnd - windowStart + 1 - maximumRepeated) > k:
                leftCharacter = s[windowStart]
                memory[leftCharacter] -= 1
                windowStart += 1
            currentLength = windowEnd - windowStart + 1
            maximumLength = max(currentLength, maximumLength)
        return maximumLength
