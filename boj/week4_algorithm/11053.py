# 생각해봐야할 점: 2중 for 문을 생각할 수 있는가?

import sys
N = int(sys.stdin.readline().strip())
A = [0] + list(map(int, sys.stdin.readline().strip().split()))

dp = [0] * (N+1)

for i in range(1, N+1):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))