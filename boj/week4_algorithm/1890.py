import sys
N = int(sys.stdin.readline().strip())

dp=[[0 for _ in range(N+1)] for _ in range(N+1)]
dp[1][1] = 1

graph = [[False]]
for _ in range(N):
    information = [0] + list(map(int, sys.stdin.readline().strip().split()))
    graph.append(information)

for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == 0:
            continue
        if i==N and j==N:
            break
        if j + graph[i][j]<=N:
            dp[i][j + graph[i][j]] += dp[i][j]
        if i + graph[i][j]<=N:
            dp[i + graph[i][j]][j] += dp[i][j]
            
print(dp[N][N])