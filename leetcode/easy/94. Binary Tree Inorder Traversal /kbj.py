# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited = []
        def dfs(root):
            if root is None:
                return root

            if root.left is not None:
                dfs(root.left)

            visited.append(root.val)

            if root.right is not None:
                dfs(root.right)

        dfs(root)

        return visited