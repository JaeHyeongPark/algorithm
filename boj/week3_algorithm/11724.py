import sys

N, M = map(int, sys.stdin.readline().strip().split())
#linked list
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0

def dfs(i):
    visited[i] = True
    for j in graph[i]:
        if visited[j] == False:
            dfs(j)


for i in range(1, N+1):
    if visited[i] == False:
        if not graph[i]:
            count+=1
            visited[i] = True
        else:
            dfs(i)
            count +=1

print(count)