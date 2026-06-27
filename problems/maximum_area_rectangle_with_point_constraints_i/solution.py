class Solution:
    def maxRectangleArea(self, points):
        ans = -1
        n = len(points)

        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2 or y1 == y2:
                    continue
                left = min(x1, x2)
                right = max(x1, x2)
                bottom = min(y1, y2)
                top = max(y1, y2)

                corners = 0
                valid = True

                for x, y in points:
                    if x < left or x > right or y < bottom or y > top:
                        continue

                    if (x == left or x == right) and (y == bottom or y == top):
                        corners += 1
                    else:
                        valid = False
                        break
                if valid and corners == 4:
                    area = (right - left) * (top - bottom)
                    ans = max(ans, area)
        return ans