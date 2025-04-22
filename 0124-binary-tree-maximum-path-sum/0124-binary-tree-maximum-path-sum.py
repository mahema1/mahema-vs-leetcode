# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #time: O(n), space: O(n)
        # we can only split once, or else we wont get a path
          # Initialize result with the value of the root
    # We'll keep track of the highest path sum seen so far
        res=root.val
        def dfs(root):
            nonlocal res # So we can update the result variable inside this scope
            if not root:
                return 0
            leftmax= dfs(root.left)
            rightmax=dfs(root.right)
            #there could be negative value
            #to calculate- i can choose to not take them.
            leftmax=max(leftmax, 0) 
            rightmax= max(rightmax, 0)
               # At this node, consider the **max path sum including both subtrees**
        # This represents the "split" — the node is a peak of the path
            current_path_sum = root.val + leftmax + rightmax


            res= max(res, current_path_sum)
             # Return the **one-sided max gain** to be used by the parent node
        # We can only choose one child to continue the path upward
            return root.val + max(leftmax, rightmax)

        dfs(root)
        return res



    