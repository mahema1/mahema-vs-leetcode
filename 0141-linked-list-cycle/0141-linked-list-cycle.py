# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow, fast= head, head

        # while fast and fast.next:
        #     slow= slow.next
        #     fast= fast.next.next
        #     if slow==fast:
        #         return True

        # return False
        seen=set()
        curr= head
        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr= curr.next
        return False
    
        