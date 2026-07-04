class Solution:
    def preorderTraversal(self, root):
        ans = []
        def preorder(node):
            if not node:
                return
            ans.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ans