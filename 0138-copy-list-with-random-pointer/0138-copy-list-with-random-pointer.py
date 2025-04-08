"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # oldToCopy={None: None}
        # curr= head
        # while curr:
        #     copy= Node(curr.val)
        #     oldToCopy[curr]= copy
        #     curr= curr.next
        # curr= head
        # while curr:
        #     copy= oldToCopy[curr]
        #     copy.next= oldToCopy[curr.next]
        #     copy.random= oldToCopy[curr.random]
        #     curr= curr.next
        # return oldToCopy[head]

        # make a node copy and make the connections
        if not head:
            return None


        curr= head
        while curr:
            copy= Node(curr.val)
            temp= curr.next
            curr.next= copy
            copy.next= temp
            curr= temp
        # assign random
        curr= head
        while curr:
            if curr.random:
                curr.next.random= curr.random.next
            else:
                curr.next.random= None
            curr= curr.next.next
        old= head
        if old:
            new= old.next
            newhead= new
        while old or new:
            old.next= old.next.next
            if new.next:
                new.next= new.next.next
            else:
                new.next= None
            old= old.next
            new= new.next
        return newhead






        # curr= head
        # while curr:
        #     copy= Node(curr.val)
        #     temp= curr.next
        #     curr.next= copy
        #     copy.next= temp
        #     curr= temp
        # #assign random

        # curr= head
        # while curr:
        #     if curr.random:
        #         curr.next.random= curr.random.next
        #     else:
        #         curr.next.random= None
        #     curr= curr.next.next
        
        # #remove the connections and put it back
        
        # old= head
        # if old:
        #     new= old.next
        #     newhead= new
        #     while old or new:

        #         old.next= old.next.next
        #         if new.next:
        #             new.next= new.next.next
        #         else:
        #             new.next= None
        #         old= old.next
        #         new= new.next
        #     return newhead


            

        