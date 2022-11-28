import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
edges = []
distance = [INF]*(v+1)

for _ in range(e):
    a, b, c = map(int, input().split())
    #a->b costs c
    edges.append((a,b,c))

def bellman_ford(start):
    distance[start] = 0
    for i in range(v):
        for j in range(e):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            edge_cost = edges[j][2]
            if distance[cur_node] != INF and distance[next_node] > distance[cur_node]+edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost
                # i: 0~v-1라운드까지, 총 v번 돈다. i=v-1,즉 v번째 라운드가 돌아간다면 negative cycle이 있다는 것.
                if i == v-1:
                    return True
    return False

#try algorithm
negative_cycle = bellman_ford(1)

if negative_cycle:
    print("-1")
else:
    for i in range(2, v+1):
        if distance[i] == INF:
            print("-1")
        else:
            print(distance[i])