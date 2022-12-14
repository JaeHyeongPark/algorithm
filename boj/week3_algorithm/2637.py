from collections import deque
import sys

N = int(sys.stdin.readline().strip()) #완제품 번호
M = int(sys.stdin.readline().strip())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N + 1)
result_matrix = [[0 for _ in range(N+1)] for _ in range(N+1)] # 결과값 담는 행렬

for _ in range(M):
    # to make X, need K units of Y
    X, Y, K = map(int, sys.stdin.readline().strip().split())
    graph[Y].append((X, K))
    indegree[X] += K

def topology_sort():
    result = [] # 다돌았는지 확인
    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        if len(result) == N:
            break
        # 해당 노드가 기본제품이라면,
        for (i, units) in graph[now]:
            indegree[i] -= units
            if sum(result_matrix[now]) == 0:
                result_matrix[i][now] += units #기본 제품이라서
            else:
                for j in range(1, N+1):
                    result_matrix[i][j] += result_matrix[now][j] * units #중간 제품이라서               
            if indegree[i] == 0:
                q.append(i)

topology_sort()
for i in range(1, N+1):
    if result_matrix[N][i] != 0:
        print(i, result_matrix[N][i])