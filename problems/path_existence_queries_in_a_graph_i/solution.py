class Solution:
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        group = [0] * n
        curr = 0
        for i in range(1, n):
            if nums[i] - nums[ i - 1] > maxDiff:
                curr += 1
            group[i] = curr
        ans = []
        for u, v in queries:
            ans.append(group[u] == group[v])
        return ans