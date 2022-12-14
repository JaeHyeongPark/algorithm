#N: stuff number
#each has W weight, value V
#maximum K weight
# maximize sum(V)
import sys
N, K = map(int, sys.stdin.readline().strip().split())

bag = [(0,0)]

for _ in range(N):
    W, V = map(int, sys.stdin.readline().strip().split())
    bag.append((W,V))

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        w = bag[i][0]
        v = bag[i][1]
        if j<w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j], dp[i-1][j-w]+v)
        print(dp)

print(dp[N][K])

