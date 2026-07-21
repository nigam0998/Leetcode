class Solution:
    def findDifferentBinaryString(self, nums):
        n = len(nums)
        s = set(nums)
        for i in range(2 ** n):
            binary = bin(i)[2:].zfill(n)
            if binary not in s:
                return binary