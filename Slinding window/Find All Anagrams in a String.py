"""
Leetcode
438. Find All Anagrams in a String
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output:
[0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"
Output:
[0, 1, 2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        memory = {}
        windowStart, matched = 0, 0
        resultIndexes = []
        for character in p:
            if character not in memory:
                memory[character] = 0
            memory[character] += 1
        for windowEnd in range(len(s)):
            rightCharacter = s[windowEnd]
            if rightCharacter in memory:
                memory[rightCharacter] -= 1
                if memory[rightCharacter] == 0:
                    matched += 1
            if matched == len(memory):
                resultIndexes.append(windowStart)
            if windowEnd >= len(p) - 1:
                leftCharacter = s[windowStart]
                windowStart += 1
                if leftCharacter in memory:
                    if memory[leftCharacter] == 0:
                        matched -= 1
                    memory[leftCharacter] += 1
        return resultIndexes
