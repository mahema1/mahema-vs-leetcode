"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # #time :O(n), space:O(n)
        # #from p to parent and q to parent 
        # seen= set()
        # while (p):
        #     seen.add(p)
        #     p= p.parent
        # while (q):
        #     if q in seen:
        #         return q
        #     else:
        #         q=q.parent

        pCopy= p
        qCopy= q

        while pCopy != qCopy:
            pCopy= pCopy.parent if pCopy else q
            qCopy= qCopy.parent if qCopy else p

        return pCopy

        

        
             
        