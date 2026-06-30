class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        temp = nums[-k:] + nums[:-k]
        for i in range(n):
            nums[i] = temp[i]