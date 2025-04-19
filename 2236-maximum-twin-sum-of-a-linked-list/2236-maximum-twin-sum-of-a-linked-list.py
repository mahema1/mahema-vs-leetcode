# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # divide it into two linkedlists, reverse the second list and then add
        #the consecutive elements and return the max
        # find the middle, so that we can have the slow point to the other head
        slow= fast= head
        while fast and fast.next:
            fast=fast.next.next
            slow= slow.next

            #1->2---------      3<-4
        #our              Null< /

        curr= slow
        prev= None
        while curr:
            temp= curr.next
            curr.next= prev
            prev= curr
            curr= temp
        head2= prev # the new head of the second list
        max_val=0
        while head2:
            max_val=max(max_val, head.val+head2.val)
            head= head.next
            head2= head2.next
        return max_val
        



        