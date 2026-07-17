from bisect import bisect_right
class Solution:
    def gcdValues(self, nums, queries):
        mx = max(nums)
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1
        gcdCnt = [0] * (mx + 1)
        for g in range(mx, 0, -1):
            count = 0
            for m in range(g, mx + 1, g):
                count += freq[m]
            gcdCnt[g] = count * (count - 1) // 2
            for m in range(2 * g, mx + 1, g):
                gcdCnt[g] -= gcdCnt[m]
        prefix = [0] * (mx + 1)
        prefix[0] = gcdCnt[0]
        for i in range(1, mx + 1):
            prefix[i] = prefix[i - 1] + gcdCnt[i]
        ans = []
        for q in queries:
            ans.append(bisect_right(prefix, q))
        return ans