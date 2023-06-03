# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return t1.val == t2.val and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

        # ---------
        if root is None:
            return True

        def isMirror2(left, right):
            if not left and not right:
                return True

            if left and right and left.val == right.val:
                return isMirror2(left.right, right.left) and isMirror2(left.left, right.right)

            return False

        # return isMirror(root, root)

        return isMirror2(root.left, root.right)
