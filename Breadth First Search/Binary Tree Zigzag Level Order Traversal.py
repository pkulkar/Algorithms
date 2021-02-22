"""
Leetcode:
103. Binary Tree Zigzag Level Order Traversal
Given the root of a binary tree, return the zigzag level order traversal of its nodes'
values. (i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        level_nodes = list(list())
        queue = deque()
        queue.append(root)
        index = 0
        while queue:
            length = len(queue)
            nodes = deque()
            for _ in range(length):
                node = queue.popleft()
                if index%2 == 0:
                    nodes.append(node.val)
                else:
                    nodes.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            index += 1
            level_nodes.append(nodes)
        return level_nodes

"""
Time Complexity: O(n) where n is number of nodes in tree
Space Complexity: O(n)
"""
