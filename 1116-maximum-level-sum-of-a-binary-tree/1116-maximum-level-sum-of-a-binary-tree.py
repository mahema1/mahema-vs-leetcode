# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q= deque()
        q.append(root)
        max_sum= -float("inf")
        max_level=0
        current=1
        while q:
            l=0
            for i in range(len(q)):
                
                node= q.popleft()
                l+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if l>max_sum:
                max_sum= l
                max_level= current
            current+=1
        return max_level
            


        
            
        