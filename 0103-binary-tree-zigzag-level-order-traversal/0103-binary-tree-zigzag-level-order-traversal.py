# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q= deque()
        if not root:
            return []
        q.append(root)
        res=[]
        while q:
            level=[]
            lenq= len(q)
            for i in range(lenq):
                node= q.popleft()
                if node:
                    level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if len(res) %2:
                level.reverse()
            res.append(level)
        return res

    