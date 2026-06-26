# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # neu danh sach chan
        if fast:
            second = slow.next
        else:
            second = slow

        prev=None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        first = head
        second = prev
        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True




        