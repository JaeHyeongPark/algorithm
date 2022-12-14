import sys
import heapq
N = int(sys.stdin.readline().strip()) # 도시개수
M = int(sys.stdin.readline().strip()) # 버스개수

graph = [[] for _ in range(N+1)]

for _ in range(M):
    #출발 도시 - 도착 도시 - 비용
    a, b, cost = map(int, sys.stdin.readline().strip().split())
    graph[a].append((b, cost))
start, end = map(int, sys.stdin.readline().strip().split())

distance = [float('INF') for _ in range(N+1)]

def Dijkstra(start):
    node = []
    distance[start] = 0
    heapq.heappush(node, (0, start))

    while node:
        dist, now = heapq.heappop(node)

        if distance[now] < dist:
            continue
        
        for (city, cost) in graph[now]:
            if dist+cost < distance[city]:
                distance[city] = dist + cost
                heapq.heappush(node, (dist+cost, city))

Dijkstra(start)
print(distance[end])