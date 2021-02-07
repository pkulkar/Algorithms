"""
Non Leetcode Question:
    https://www.educative.io/courses/grokking-the-coding-interview/YQQwQMWLx80
        Given a string, find the length of the longest substring in it with no more than K distinct characters.

        Example 1:

        Input: String="araaci", K=2
        Output: 4
        Explanation: The longest substring with no more than '2' distinct characters is "araa".
        Example 2:

        Input: String="araaci", K=1
        Output: 2
        Explanation: The longest substring with no more than '1' distinct characters is "aa".
        Example 3:

        Input: String="cbbebi", K=3
        Output: 5
        Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
"""

def longest_substring_with_k_distinct(str, k):
  longestLength, windowStart = 0, 0
  memory = {}
  for windowEnd in range(len(str)):
    currentChar = str[windowEnd]
    if currentChar not in memory:
      memory[currentChar] = 0
    memory[currentChar] += 1
    while len(memory) > k:
      character = str[windowStart]
      memory[character] -= 1
      if memory[character] == 0:
        del memory[character]
      windowStart += 1
    currentLength = windowEnd - windowStart + 1
    longestLength = max(longestLength, currentLength)
  return longestLength
