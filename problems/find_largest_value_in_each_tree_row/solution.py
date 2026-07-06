from collections import deque
class Solution:
    def largestValues(self, root):
        if not root:
            return []
        ans = []
        q = deque([root])
        while q:
            size = len(q)
            maximum = q[0].val
            for i in range(size):
                node  = q.popleft()
                if node.val > maximum:
                    maximum = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(maximum)
        return ans