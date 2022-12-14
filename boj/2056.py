import sys
from collections import deque

N = int(sys.stdin.readline().strip())

graph = [[] for _ in range(N+1)]
value = [0]
visited = [False for _ in range(N+1)]
dp = [0 for _ in range(N+1)]

start_node = 0
for i in range(1, N+1):
    input_list = list(map(int, sys.stdin.readline().split()))
    value.append(input_list[0])
    for j in range(input_list[1]):
        graph[input_list[2+j]].append(i)
    if input_list[1] == 0:
        start_node = i

q = deque()
q.append(start_node)
dp[start_node] = value[start_node]

while visited.count(True) != N:
    x = q.popleft()
    if visited[x] != True:
        for next_node in graph[x]:
            if dp[next_node] < dp[x] + value[next_node]:
                dp[next_node] = dp[x] + value[next_node]
        visited[x] = True
    for new_node in graph[x]:
        q.append(new_node)

print(dp[N])