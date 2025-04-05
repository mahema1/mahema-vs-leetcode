# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow= fast= head
        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next
            if slow== fast:
                # slow= slow.next
                break
        if not fast or not fast.next:
            return None
        
        curr= head
        while curr!=slow:
            curr=curr.next
            slow=slow.next

        return curr
        