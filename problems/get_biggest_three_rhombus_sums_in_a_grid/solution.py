class Solution:
    def getBiggestThree(self, grid):
        m = len(grid)
        n = len(grid[0])
        s = set()

        for i in range(m):
            for j in range(n):
                s.add(grid[i][j])
                d = 1
                while True:
                    if i - d < 0 or i + d >= m or j - d < 0 or j + d >= n:
                        break
                    total = 0
                    x = i - d
                    y = j
                    for k in range(d):
                        total += grid[x + k][y + k]
                    x = i
                    y = j + d
                    for k in range(d):
                        total += grid[x + k][y - k]
                    x = i + d
                    y = j
                    for k in range(d):
                        total += grid[x - k][y - k]
                    x = i
                    y = j - d
                    for k in range(d):
                        total += grid[x - k][y + k]
                    s.add(total)
                    d += 1
        ans = sorted(s, reverse=True)
        return ans[:3]