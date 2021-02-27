"""
Leetcode
437. Path Sum III
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.recursive_pathSum(root, sum, [])

    def recursive_pathSum(self, node, target, currentPath):
        if not node:
            return 0
        currentPath.append(node.val)
        pathCount, pathSum = 0, 0
        for i in range(len(currentPath)- 1, -1, -1):
            pathSum += currentPath[i]
            if pathSum == target:
                pathCount += 1

        pathCount += self.recursive_pathSum(node.left, target, currentPath)
        pathCount += self.recursive_pathSum(node.right, target, currentPath)
        del currentPath[-1]
        return pathCount
