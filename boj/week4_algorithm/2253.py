# import sys
# from math import sqrt
# #N은 전체 돌 개수, M은 크기가 작은 돌 개수
# N, M = map(int, sys.stdin.readline().strip().split())
# dp=[[float('INF') for _ in range(N+1)] for _ in range(N+1)]
# dp[1][0] = 0

# small_rocks = []
# for _ in range(M):
#     impossible_idx = int(sys.stdin.readline().strip())
#     small_rocks.append(impossible_idx)

# for i in range(2, N+1):
#     if i in small_rocks:
#         continue
#     for v in range(1, int(1/2 + sqrt(8*i-7)/2)):
#         dp[i][v] = min(dp[i-v][v-1], dp[i-v][v], dp[i-v][v+1]) + 1

# a=min(dp[N])

# if a == float('INF'):
#     print(-1)
# else:
#     print(a)

from sys import stdin
from math import sqrt
input = stdin.readline

def solve():
    N, M = map(int, input().split())
    dp = [[float('inf')] * (int(sqrt(2*N))+2) for _ in range(N+1)]
    dp[1][0] = 0
    trap = set()
    for _ in range(M):
        trap.add(int(input()))
    
    for i in range(2, N+1):
        if i in trap:
            continue
        for v in range(1, int(sqrt(2*i)) + 1): # v 범위를 제한 => 들어오는 i에 대해서만
            dp[i][v] = min(dp[i-v][v-1], dp[i-v][v], dp[i-v][v+1]) + 1
    
    result = min(dp[N])
    if result == float('inf'):
        print(-1)
    else:
        print(result)

solve()