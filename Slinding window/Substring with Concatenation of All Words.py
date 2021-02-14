"""
Leetcode
30. Substring with Concatenation of All Words

You are given a string s and an array of strings words of the same length.
Return all starting indices of substring(s) in s that is a concatenation of
each word in words exactly once, in any order, and without any intervening characters.
You can return the answer in any order.

Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]

Constraints:
1 <= s.length <= 104
s consists of lower-case English letters.
1 <= words.length <= 5000
1 <= words[i].length <= 30
words[i] consists of lower-case English letters.
"""
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not words[0]:
            return []
        wordFrequency = {}
        for word in words:
            if word not in wordFrequency:
                wordFrequency[word] = 0
            wordFrequency[word] += 1

        resultIndices = []
        wordsCount = len(words)
        wordLength = len(words[0])
        for i in range((len(s) - wordsCount * wordLength) + 1):
            wordsSeen = {}
            for j in range(0, wordsCount):
                nextIndex = i + j * wordLength
                word = s[nextIndex: nextIndex + wordLength]
                if word not in wordFrequency:
                    break
                if word not in wordsSeen:
                    wordsSeen[word] = 0
                wordsSeen[word] += 1
                if wordsSeen[word] > wordFrequency.get(word, 0):
                    break
                if j+1 == wordsCount:
                    resultIndices.append(i)
        return resultIndices
