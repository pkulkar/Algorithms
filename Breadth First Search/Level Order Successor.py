"""
Non Leetcode:
Given a binary tree and a node, find the level order successor of the given node in the tree.
The level order successor is the node that appears right after the given node in the level order traversal.
"""
from collections import deque
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):
  # TODO: Write your code here
  if not root:
    return None
  queue = deque()
  queue.append(root)
  is_found = False
  while queue:
    length = len(queue)
    for _ in range(length):
      node = queue.popleft()
      if is_found:
        return node
      if node.val == key:
        is_found = True
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
  return None


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  result = find_successor(root, 12)
  if result:
    print(result.val)
  result = find_successor(root, 9)
  if result:
    print(result.val)


main()

"""
Time Complexity: O(n) where n is number of nodes in tree
Space Complexity: O(n)
"""
