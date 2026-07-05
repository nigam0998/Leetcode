class Solution:
    def pathSum(self, root, targetSum):
        ans = []
        def dfs(node, target, path):
            if not node:
                return
            path.append(node.val)
            target -= node.val
            if not node.left and not node.right:
                if target == 0:
                    ans.append(path[:])
            else:
                dfs(node.left, target, path)
                dfs(node.right, target, path)
            path.pop()
        dfs(root, targetSum, [])
        return ans