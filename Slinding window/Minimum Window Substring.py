"""
Leetcode
76. Minimum Window Substring
Given two strings s and t, return the minimum window in s which will contain all
the characters in t. If there is no such window in s that covers all characters
in t, return the empty string "". Note that If there is such a window, it is
guaranteed that there will always be only one unique minimum window in s.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Example 2:
Input: s = "a", t = "a"
Output: "a"

Constraints:
1 <= s.length, t.length <= 105
s and t consist of English letters.

Follow up: Could you find an algorithm that runs in O(n) time?
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        windowStart, matched, stringStart = 0, 0, 0
        memory = {}
        minimumLength = len(s) + 1
        for character in t:
            if character not in memory:
                memory[character] = 0
            memory[character] += 1
        for windowEnd in range(len(s)):
            rightCharacter = s[windowEnd]
            if rightCharacter in memory:
                memory[rightCharacter] -= 1
                if memory[rightCharacter] >= 0:
                    matched += 1
            while matched == len(t):
                if minimumLength > windowEnd - windowStart + 1:
                    minimumLength = windowEnd - windowStart + 1
                    stringStart = windowStart
                leftCharacter = s[windowStart]
                windowStart += 1
                if leftCharacter in memory:
                    if memory[leftCharacter] == 0:
                        matched -= 1
                    memory[leftCharacter] += 1
        if minimumLength > len(s):
            return ""
        return s[stringStart:stringStart + minimumLength]
