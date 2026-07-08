class Solution:
    def minimumDistance(self, nums):
        pos = {}
        for i in range(len(nums)):
            if nums[i] not in pos:
                pos[nums[i]] = []
            pos[nums[i]].append(i)
        ans = float("inf")
        for indexes in pos.values():
            if len(indexes) < 3:
                continue
            for i in range(len(indexes) - 2):
                a = indexes[i]
                b = indexes[i + 1]
                c = indexes[i + 2]
                dist = abs(a - b) + abs(b - c) + abs(c - a)
                ans = min(ans, dist)
        if ans == float("inf"):
            return -1
        return ans