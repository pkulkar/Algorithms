"""
Leetcode
567. Permutation in String
Given two strings s1 and s2, write a function to return true if s2 contains the
permutation of s1. In other words, one of the first string's permutations is the
substring of the second string.

Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False

Constraints:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        memory = {}
        windowStart, matched = 0, 0
        for character in s1:
            if character not in memory:
                memory[character] = 0
            memory[character] += 1
        for windowEnd in range(len(s2)):
            rightCharacter = s2[windowEnd]
            if rightCharacter in memory:
                memory[rightCharacter] -= 1
                if memory[rightCharacter] == 0:
                    matched += 1
            if matched == len(memory):
                return True
            if windowEnd >= len(s1) - 1:
                leftCharacter = s2[windowStart]
                windowStart += 1
                if leftCharacter in memory:
                    if memory[leftCharacter] == 0:
                        matched -= 1
                    memory[leftCharacter] += 1
        return False
