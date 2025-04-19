# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #    eh  
        #                e
        # 1->2->3->4->5
        #             o
        # 1->3->5->2->4
        if not head:
            return None
        if not head.next:
            return head
        odd= head
        even= even_head= head.next
        while even and even.next:
            odd.next= even.next
            odd= odd.next
            even.next= odd.next
            even=even.next
        odd.next= even_head
        return head

        