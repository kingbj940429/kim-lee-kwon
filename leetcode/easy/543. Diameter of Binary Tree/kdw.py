# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            nonlocal answer

            if not root:
                return 0

            left, right = depth(root.left), depth(root.right)
            answer = max(answer, left + right)
            return max(left, right) + 1

        answer = 0
        depth(root)
        return answer
