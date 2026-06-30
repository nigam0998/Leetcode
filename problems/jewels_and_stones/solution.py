class Solution:
    def numJewelsInStones(self, jewels, stones):
        jewelSet = set(jewels)
        count = 0

        for ch in stones:
            if ch in jewelSet:
                count += 1
        return count