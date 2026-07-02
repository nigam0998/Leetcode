class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        n = len(matrix[0])
        heights = [0] * n
        ans = 0
        for row in matrix:
            for i in range(n):
                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0
            ans = max(ans, self.largestRectangle(heights))
        return ans
    
    def largestRectangle(self, heights):
        stack = []
        area = 0
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i
                area = max(area, h * w)
            stack.append(i)
        heights.pop()
        return area