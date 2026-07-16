class Solution(object):
    def zigZagArrays(self, n, l, r):
        MOD = 10**9 + 7
        m = r - l + 1
        states = 2 * m
        T = [[0] * states for _ in range(states)]
        for x in range(m):
            downState = x
            upState = x + m 
            for y in range(x + 1, m):
                T[y][upState] = 1    
            for y in range(x):
                T[y + m][downState] = 1     
        def multiply(A, B):
            C = [[0] * states for _ in range(states)]
            for i in range(states):
                for k in range(states):
                    if A[i][k] == 0: 
                        continue
                    for j in range(states):
                        if B[k][j] == 0: 
                            continue
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C
        def power(base, exp):
            res = [[0] * states for _ in range(states)]
            for i in range(states):
                res[i][i] = 1
            while exp > 0:
                if exp % 2 == 1:
                    res = multiply(res, base)
                base = multiply(base, base)
                exp //= 2
            return res 
        P = power(T, n - 1)
        start = [1] * states
        ans = 0
        for i in range(states):
            for j in range(states):
                ans = (ans + P[i][j] * start[j]) % MOD      
        return ans