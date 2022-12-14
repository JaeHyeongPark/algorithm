import sys
from sys import setrecursionlimit

setrecursionlimit(2*10**5)

N = int(sys.stdin.readline().strip())
location = [0] + list(map(int, sys.stdin.readline().strip()))

graph = [ [] for _ in range(N+1) ]
visited = [ False for _ in range(N+1) ]
ans = 0

# 실외 노드를 기준으로 think. 실내 노드들이 인접해있을 때 따로 세고
# 실외 노드끼리 연결되는 케이스도 따로 생각!
# 실내 노드끼리 연결되는 것도 따로 체크

# 0: 실외, 1: 실내

for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)
    #실내노드끼리 바로 연결
    if location[u] == 1 and location[v] == 1:
        ans += 2

def dfs(v, cnt): # 인접한 실내 노드 개수 가지고 있게; cnt를 재귀에서 넘겨줘야하는 것이 또 포인트...
    visited[v] = True
    for i in graph[v]:
        if location[i] == 1:
            cnt+=1
        elif location[i] == 0 and visited[i] == False:
            cnt = dfs(i, cnt)
    return cnt

for i in range(1, N+1):
    if location[i] == 0 and visited[i] == False:
        c = dfs(i, 0)
        ans += c*(c-1)

print(ans)