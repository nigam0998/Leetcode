class Solution:
    def postorderTraversal(self, root):
        ans = []
        def postorder(node):
            if not node:
                return
            postorder(node.left)
            postorder(node.right)
            ans.append(node.val)
        postorder(root)
        return ans