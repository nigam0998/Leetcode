class Solution:
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7
        n = len(s)
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
        prefix_sum = [0] * (n + 1)
        prefix_cnt = [0] * (n + 1)
        prefix_num = [0] * (n + 1)
        for i in range(n):
            digit = int(s[i])
            prefix_sum[i + 1] = prefix_sum[i]
            prefix_cnt[i + 1] = prefix_cnt[i]
            prefix_num[i + 1] = prefix_num[i]
            if digit != 0:
                prefix_sum[i + 1] += digit
                prefix_cnt[i + 1] += 1
                prefix_num[i + 1] = (prefix_num[i] * 10 + digit) % MOD
        ans = []
        for l, r in queries:
            digit_sum = prefix_sum[r + 1] - prefix_sum[l]
            cnt = prefix_cnt[r + 1] - prefix_cnt[l]
            x = (
                prefix_num[r + 1] - prefix_num[l] * pow10[cnt]
            ) % MOD
            ans.append((x * digit_sum) % MOD)
        return ans