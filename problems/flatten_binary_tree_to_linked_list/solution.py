class Solution:
    def flatten(self, root):
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            temp = root.right
            root.right = root.left
            root.left = None
            curr = root.right
            while curr.right:
                curr = curr.right
            curr.right = temp