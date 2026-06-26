# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ý tưởng: Cho fast đi trước n bước, 
# thì slow đứng trước node cần xóa -> slow.next = slow.next.next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0) # node giả, nơi sẽ chứa các node đã xử lý xong
        dummy.next = head

        slow=dummy
        fast=dummy
        
        for _ in range (n+1):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next



