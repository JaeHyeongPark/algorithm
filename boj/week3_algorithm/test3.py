import sys
from heapq import heappop, heappush
from collections import deque
#1<=N<=200, 1<=K<=1000; K개의 바이러스;
N, K = map(int, sys.stdin.readline().strip().split())

graph = [[] for _ in range(N+1)]

for i in range(1, N+1):
    graph[i] = [False] + list(map(int, sys.stdin.readline().strip().split()))

S, X, Y = map(int, sys.stdin.readline().strip().split())
#S초 뒤에 (x,y)에 있는 바이러스 구하기

virus_list = deque()
temp_list = []
for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == 0:
            continue
        else:
            temp_list.append((graph[i][j], 0, i, j))

temp_list.sort()

for k in temp_list:
    virus_list.append(k)

dx = [0, 0, -1, 1]
dy = [1, -1, 0 ,0]

while virus_list:
    virus_idx, time, x, y = virus_list.popleft()
    if time == S:
        break
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 1<=ny<=N and 1<=nx<=N:
            if graph[nx][ny] != 0:
                continue
            graph[nx][ny] = virus_idx
            virus_list.append((virus_idx, time+1, nx, ny))

print(graph[X][Y])



