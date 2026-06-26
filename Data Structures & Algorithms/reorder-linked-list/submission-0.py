# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# chia đôi (tìm mid) -> revverse nửa sau -> merge 
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head
        prev=None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # khi fast = None thì slow ở đâu chính là mid ở đó

        second = slow.next
        slow.next = None
        prev = None
        
        # reverse
        while second: # ví dụ: 5->6->7
            next_node = second.next
            second.next = prev # ngắt node ra, list1= 5-> None, list2= 6->7
            prev = second
            second = next_node
        
        # merge
        first, second = head, prev
        while first and second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
            


            



            



        