class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        current = 0
        down = False

        for ch in s:
            rows[current] += ch

            if current == 0 or current == numRows - 1:
                down = not down

            if down:
                current += 1
            else:
                current -= 1

        return "".join(rows)