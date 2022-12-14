import sys
n = int(sys.stdin.readline().strip())

dp = [0]*91

dp[1]=1

def fibo(x):
    if x == 0:
        return 0
    if dp[x] != 0:
        return dp[x]
    else:
        dp[x] = fibo(x-1) + fibo(x-2)
        return dp[x]

print(fibo(n))