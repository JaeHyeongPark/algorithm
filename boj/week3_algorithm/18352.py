import sys
from collections import deque
from heapq import heappush, heappop

#N: 도시 개수, M: 도로 개수, K: 최단거리, X: 출발도시
N, M, K, X = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split()) # a to b
    graph[a].append(b)

distance = [float('INF') for _ in range(N+1)]
visited = [False for _ in range(N+1)]

# dijkstra algorithm
def Dijkstra(N, start):
    node = []
    distance[start] = 0
    visited[start] = True
    heappush(node, (0, start))

    while node:
        dist, now = heappop(node)

        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            if dist+1 < distance[i]:
                distance[i] = dist + 1
                heappush(node, (dist+1, i))

Dijkstra(N, X)
# print('Dij', distance)
count = 0
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        count +=1
if count == 0:
    print(-1)