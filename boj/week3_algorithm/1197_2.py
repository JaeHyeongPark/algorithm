import heapq
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v,e = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(v+1)]
edges = [[] for _ in range(v+1)]

for i in range(e):
    x, y, weight = map(int, sys.stdin.readline().split())
    edges[x].append([weight, y])
    edges[y].append([weight, x])

heap=[]
answer = 0
cnt = 0

heap.append([0,1])

while cnt < v:
    weight, node = heapq.heappop(heap)
    if visited[node] == 0:
        visited[node] = True
        answer += weight
        cnt+=1
        for i in edges[node]:
            heapq.heappush(heap, i)

print(answer)