from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        ans = []
        q = deque([root])
        leftToRight = True

        while q:
            level = []
            size = len(q)

            for i in range(size):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            if not leftToRight:
                level.reverse()

            ans.append(level)
            leftToRight = not leftToRight

        return ans