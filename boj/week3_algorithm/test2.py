import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
#세로, 가로
# '-‘와 ’|
visited = [[False for _ in range(M+1)] for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    graph[i]=[False] + list(input().strip())+[False]

cnt = 0

for i in range(1, N+1):
    for j in range(1, M+1):
        if graph[i][j] == '-':
            if graph[i][j+1] == '-':
                continue
            cnt+=1
        elif graph[i][j] == '|':
            visited[i][j] = True
            ny = i-1
            if visited[ny][j] == True and graph[ny][j] == '|':
                continue
            cnt+=1   

print(cnt)