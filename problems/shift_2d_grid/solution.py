class Solution:
    def shiftGrid(self, grid, k):
        rows = len(grid)
        cols = len(grid[0])
        arr = []
        for row in grid:
            for num in row:
                arr.append(num)
        k = k % len(arr)
        arr = arr[-k:] + arr[:-k]
        result = []
        index = 0
        for i in range(rows):
            temp = []
            for j in range(cols):
                temp.append(arr[index])
                index += 1
            result.append(temp)
        return result