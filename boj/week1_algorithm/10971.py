# N: 2~10
# matrices: 0 ~ 1,000,000
import sys
N = int(sys.stdin.readline())
W = [[] for _ in range(N)]
visited = [False for _ in range(N)]

for i in range(N):
    W[i] = list(map(int, sys.stdin.readline().split(" ")))

result = N*N*1000000
cost = 0

#start: 시작도시, now: 현재 도시
def calCost(start, now, visitedNum):
    global result
    global cost
    if visitedNum == N and now == start:
        result = min(result, cost)
        return
    for i in range(N):
        if visited[i] == False and W[now][i]>0:
            visited[i] = True
            cost += W[now][i]
            if cost <= result:
                calCost(start, i, visitedNum+1)
            visited[i] = False
            cost -= W[now][i]

for i in range(N):
    calCost(i, i, 0)

print(result)