# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head.next:
            return head

            
        slow, fast= head, head.next
        while fast.next and fast.next.next:
            slow= slow.next
            fast= fast.next.next

        return slow.next

        