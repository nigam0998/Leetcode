class Solution:
    def countAndSay(self, n):
        s = "1"
        for i in range(n - 1):
            temp = ""
            count = 1
            for j in range(1, len(s)):
                if s[j] == s[j - 1]:
                    count += 1
                else:
                    temp += str(count) + s[j - 1]
                    count = 1
            temp += str(count) + s[-1]
            s = temp

        return s