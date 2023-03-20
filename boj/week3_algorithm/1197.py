#Kruskal
import sys
#V, E
V, E = map(int, sys.stdin.readline().strip().split())
parents = [i for i in range(V+1)]
# E개의 간선에 대한 정보 받기
edges=[]
sumOfEdges = 0

for _ in range(E):
    a, b, cost = map(int, sys.stdin.readline().strip().split())
    edges.append((cost, a, b))

# 크루스칼 핵심: edges들이 정렬되어 있어야 함. 여기서 시간복잡도를 줄여야.
edges.sort()

def find(parents, x):
    if parents[x] != x:
        return find(parents, parents[x])
    return parents[x]

def union(parents, a, b):
    parents_a = find(parents, a)
    parents_b = find(parents, b)
    if parents_a < parents_b:
        parents[parents_b] = parents_a
    else:
        parents[parents_a] = parents_b

for i in range(E):
    cost, a, b = edges[i]
    if find(parents, a) != find(parents, b):
        union(parents, a, b)
        sumOfEdges += cost

print(sumOfEdges)
