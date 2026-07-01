class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        mp = {}
        for num in nums2:
            while stack and num > stack[-1]:
                mp[stack.pop()] = num
            stack.append(num)
        while stack:
            mp[stack.pop()] = -1
        ans = []
        for num in nums1:
            ans.append(mp[num])
        return ans