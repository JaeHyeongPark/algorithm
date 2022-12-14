#정점 개수 N <= 1000, 간선 개수 M <= 10000, 시작 정점 V
import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().strip().split())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited_dfs = [ False for _ in range(N+1)]
visited_bfs = [ False for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    graph[i][j], graph[j][i] = 1, 1

def dfs(node):
    stack = [node]
    while stack:
        i = stack.pop()
        if visited_dfs[i] != True:
            print(i, end=" ")
            visited_dfs[i] = True
        for j in range(len(graph[i])-1, -1, -1):
            if graph[i][j] == 1 and visited_dfs[j] == False:
                stack.append(j)

def bfs(node):
    q = deque()
    q.append(node)
    while q:
        i = q.popleft()
        if visited_bfs[i] != True:
            print(i, end=" ")
            visited_bfs[i] = True
        for j in range(len(graph[i])):
            if graph[i][j] == 1 and visited_bfs[j] == False:
                q.append(j)


dfs(V)
print()
bfs(V)