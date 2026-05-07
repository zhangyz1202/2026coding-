# week11-4.py 學習計畫 Binary Search Tree 最後1題
# LeetCode 450. Delete Node in a BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findRightest(root):
            if root.right:
                return findRightest(root.right)
            return root

        if root==None: return root
        if root.val==key:
            if root.left:
                now = findRightest(root.left)
                root.val = now.val
                root.left = self.deleteNode(root.left,now.val)
            else:
                return root.right
        root.left =self.deleteNode(root.left,key)
        root.right =self.deleteNode(root.right,key)
        return root
