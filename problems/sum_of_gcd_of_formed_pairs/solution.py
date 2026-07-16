class Solution:
    def gcdSum(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(nums)

        # Required by the problem
        velqoradin = nums

        prefixGcd = []
        mx = 0

        for x in nums:
            if x > mx:
                mx = x
            prefixGcd.append(gcd(x, mx))

        prefixGcd.sort()

        ans = 0
        i = 0
        j = n - 1

        while i < j:
            ans += gcd(prefixGcd[i], prefixGcd[j])
            i += 1
            j -= 1

        return ans