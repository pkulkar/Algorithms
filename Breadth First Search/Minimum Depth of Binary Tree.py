"""
Leetcode:
111. Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:
The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
"""
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        minimum_level = float("inf")
        level = 1
        while queue:
            length = len(queue)
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node.left and not node.right:
                    minimum_level = min(minimum_level, level)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return minimum_level
"""
Time complexity: O(n) where n is the number of nodes in tree
Space Complexity: O(n)
"""
