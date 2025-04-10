# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # #DFS
        # if not root:
        #     return 0
        # return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))

        # time : O(n), space: O(n)
        #BFS
        q= deque()
        level=0
        if root:
            q.append(root)
        while q:
            for i in range(len(q)):
                node= q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        return level
        