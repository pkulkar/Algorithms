"""
Leetcode:
112. Path Sum
Given the root of a binary tree and an integer targetSum, return true if the tree
has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false

Example 3:
Input: root = [1,2], targetSum = 0
Output: false

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        stack = []
        stack.append((root,0))
        while stack:
            node, current_sum = stack.pop()
            current_sum += node.val
            if current_sum == targetSum and (node.left is None and node.right is None):
                return True
            if node.right:
                stack.append((node.right, current_sum))
            if node.left:
                stack.append((node.left, current_sum))
        return False
"""
Time Complexity: O(n) where n is number of nodes in tree
Space Complexity: O(n)
"""
