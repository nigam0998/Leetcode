import heapq
class Solution:
    def findMaxValueOfEquation(self, points, k):
        heap = []
        ans = float("-inf")

        for x, y in points:
            while heap and x - heap[0][1] > k:
                heapq.heappop(heap)

            if heap:
                ans = max(ans, x + y - heap[0][0])

            heapq.heappush(heap, (x - y, x))
        return ans