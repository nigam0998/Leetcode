class Solution:
    def getKth(self, lo, hi, k):
        power = {1: 0}

        def steps(x):
            if x in power:
                return power[x]
            if x % 2 == 0:
                power[x] = 1 + steps(x // 2)
            else:
                power[x] = 1 + steps(3 * x + 1)
            
            return power[x]
        
        arr = []

        for num in range(lo, hi + 1):
            arr.append((steps(num), num))
        
        arr.sort()

        return arr[k - 1][1]