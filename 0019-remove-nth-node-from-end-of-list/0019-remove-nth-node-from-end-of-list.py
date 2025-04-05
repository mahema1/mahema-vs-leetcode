# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def getLength(head):
            length=0
            while head:
                length+=1
                head= head.next
            return length

        length= getLength(head)
        print(length)
        k= length- n
        print(k)

        if k==0:
            return head.next

        curr= head
        count=0
        while curr:
            if count==k-1:
                if curr.next:
                    curr.next= curr.next.next
                    break
            curr=curr.next
            count+=1
        return head



