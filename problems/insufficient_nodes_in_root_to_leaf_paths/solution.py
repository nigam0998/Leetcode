class Solution:
    def sufficientSubset(self, root, limit):

        def dfs(node, total):
            if not node:
                return None
            
            total += node.val

            if not node.left and not node.right:
                if total < limit:
                    return None
                return node
            
            node.left = dfs(node.left, total)
            node.right = dfs(node.right, total)

            if not node.left and not node.right:
                return None
            return node
        return dfs(root, 0)