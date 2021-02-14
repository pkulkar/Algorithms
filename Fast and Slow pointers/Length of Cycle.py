"""
Problem: Given the head of a LinkedList with a cycle, find the length of the cycle.
Solution: We can use the above solution to find the cycle in the LinkedList.
Once the fast and slow pointers meet, we can save the slow pointer and iterate
the whole cycle with another pointer until we see the slow pointer again to find
the length of the cycle.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return slow
        return 0
    def lengthCycle(self, head):
        current = head
        length = 0
        while True:
            current = current.next
            length += 1
            if current == head:
                return length
