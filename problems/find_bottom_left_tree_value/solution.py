from collections import deque
class Solution:
    def findBottomLeftValue(self, root):
        q = deque([root])
        ans = root.val
        while q:
            size = len(q)
            ans = q[0].val
            for i in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans