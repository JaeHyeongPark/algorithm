import sys
from collections import deque
N = int(sys.stdin.readline().strip())
p = int(sys.stdin.readline().strip())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(p):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)
count = -1
def bfs(v):
    global count
    visited[v] = True
    q = deque()
    q.append(v)

    while q:
        x = q.popleft()
        count += 1
        if graph[x]:
            for i in range(len(graph[x])):
                if visited[graph[x][i]] == False:
                    q.append(graph[x][i])
                    visited[graph[x][i]] = True
bfs(1)
print(count)
