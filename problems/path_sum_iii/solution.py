class Solution:
    def pathSum(self, root, targetSum):
        def count(node, target):
            if not node:
                return 0
            ans = 0
            if node.val == target:
                ans += 1
            ans += count(node.left, target - node.val)
            ans += count(node.right, target - node.val)
            return ans
        if not root:
            return 0
        return (
            count(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
        )