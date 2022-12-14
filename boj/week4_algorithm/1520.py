import sys

M,N = map(int, sys.stdin.readline().strip().split())
graph = [[False]]

for _ in range(M):
    info = [0]+list(map(int, sys.stdin.readline().strip().split()))
    graph.append(info)

mm = [[-1 for _ in range(N+1)] for _ in range(M+1)]

def dfs(row, col):
    global result
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]

    if row == 0 and col == 0:
        return 1
    if mm[row][col] != -1:
        return mm[row][col]
    mm[row][col] = 0
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if (
            1<=nr<=M
            and 1<=nc<=N
            and graph[nr][nc] > graph[row][col]
        ):
            mm[row][col] += dfs(nr,nc)
    return mm[row][col]

result = dfs(M, N)
print(result)