# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head

        for i in range(n-1):
            fast = fast.next

        prev = None
        while fast.next:
            fast = fast.next
            prev = slow
            slow = slow.next


        if slow == head: return head.next
        elif slow == fast:
            prev.next = None
            return head
        else:
            prev.next = slow.next
            return head