#R행 C열
# 비어있는곳 . 물차있는곳 * 돌은 X 굴은 D, 도치 위치는 S
import sys
from collections import deque

R, C = map(int, sys.stdin.readline().strip().split())
map = [[False * (C+1)]]
days = [[float('INF') for _ in range(C+1)] for _ in range(R+1)]
for _ in range(R):
    map.append([False]+list(input().strip()))

q = deque()

for y in range(1, R+1):
    for x in range(1, C+1):
        if map[y][x]=='S':
            q.append((0,y,x))
        elif map[y][x]=='D':
            D_y, D_x = y, x
for y in range(1, R+1):
    for x in range(1, C+1):
        if map[y][x]=='*':
            q.append((0,y,x))

dx = [0,0,1,-1]
dy = [1,-1,0,0]
result = float('INF')

while q:
    day, y, x = q.popleft()
    if map[D_y][D_x] == 'S':
        result = min(result, days[D_y][D_x])
        break
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 1<=nx<=C and 1<=ny<=R:
            #도치일 때
            if (map[ny][nx] == '.' or map[ny][nx] == 'D') and map[y][x] == 'S':
                map[ny][nx] = 'S'
                days[ny][nx] = day + 1
                q.append((day+1, ny, nx))
            #물일 때
            elif (map[ny][nx] == '.' or map[ny][nx] == 'S') and map[y][x] == '*':
                map[ny][nx] = '*'
                q.append((0, ny, nx))

if result == float('INF'):
    print('KAKTUS')
else:
    print(result)
