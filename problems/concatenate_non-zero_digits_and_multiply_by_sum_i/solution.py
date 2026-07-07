class Solution:
    def sumAndMultiply(self, n):
        num = ""
        total = 0
        for digit in str(n):
            if digit != "0":
                num += digit
                total += int(digit)
        if num == "":
            return 0
        return int(num) * total