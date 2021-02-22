"""
Leetcode:
257. Binary Tree Paths
Given a binary tree, return all root-to-leaf paths.
Note: A leaf is a node with no children.

Example:
Input:

   1
 /   \
2     3
 \
  5
Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        stack = []
        paths = []
        stack.append((root, ""))
        while stack:
            node, path = stack.pop()
            path = path + str(node.val)
            if not node.left and not node.right:
                paths.append(path)
                continue
            if node.left:
                new_path = path + "->"
                stack.append((node.left, new_path))
            if node.right:
                new_path = path + "->"
                stack.append((node.right, new_path))
        return paths

"""
Time Complexity: O(n) where n is number of nodes in tree
Space Complexity: O(n)
"""
