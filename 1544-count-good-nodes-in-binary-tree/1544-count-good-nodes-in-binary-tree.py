# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        #DFS time: O(n), space: O(n)
        self.good=0
        def dfs(node, maxVal):
            if node.val >= maxVal:
                self.good+=1
            if node.left:
                dfs(node.left, max(maxVal, node.val))
            if node.right:
                dfs(node.right, max(maxVal, node.val))
        dfs(root, root.val)
        return self.good
            
        

        # #BFS
        # res=0
        # q= deque()
        # if not root:
        #     return 0
        # q.append((root, root.val))
        # while q:
        #     node, maxVal= q.popleft()

        #     if node.val >= maxVal:
        #         res+=1
        #     maxVal= max(maxVal, node.val)
        #     if node.left:
        #         q.append((node.left, maxVal))
        #     if node.right:
        #         q.append((node.right, maxVal))
        # return res

