# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        slow = second
        
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        currentNode = head
        while prev:
            fnxt = currentNode.next
            currentNode.next = prev

            lnxt = prev.next
            prev.next = fnxt

            currentNode = fnxt
            prev = lnxt
            
        