# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def checkRecursively(a, b):
            return (not a and not b) or (a and b
                                         and a.val == b.val
                                         and checkRecursively(a.left, b.right) and checkRecursively(a.right, b.left))

        def checkIteratively(a, b):
            stack = [(a, b)]
            while stack:
                a, b = stack.pop()
                if not a and not b:
                    continue
                if a and b and a.val == b.val:
                    stack.append((a.right, b.left))
                    stack.append((a.left, b.right))
                else:
                    return False
            return True

        # return checkRecursively(root, root)
        return checkIteratively(root, root)
