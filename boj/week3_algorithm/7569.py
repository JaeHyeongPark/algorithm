import sys
from collections import deque

# M, N, H
M, N, H = map(int, sys.stdin.readline().strip().split())
tomato_box = [[]]
for h in range(1, H+1):
    tomato_box.append([])
    tomato_box[h].append([])
    for _ in range(N):
        tomato_box[h].append([False]+list(map(int, sys.stdin.readline().strip().split())))

q = deque()
for h in range(1,H+1):
    for y in range(1, N+1):
        for x in range(1, M+1):
            if tomato_box[h][y][x] == 1:
                q.append((0,h,y,x))

dh = [0,0,0,0,1,-1]
dy = [0,0,1,-1,0,0]
dx = [1,-1,0,0,0,0]

def bfs(q):
    result_day = 0
    while q:
        day, h, y, x = q.popleft()
        for i in range(6):
            nh=h+dh[i]
            ny=y+dy[i]
            nx=x+dx[i]
            if nh<1 or nh>H or nx<1 or nx>M or ny<1 or ny>N:
                continue
            temp = day + 1
            if tomato_box[nh][ny][nx] == -1:
                continue    
            elif tomato_box[nh][ny][nx] == 0:
                tomato_box[nh][ny][nx] = temp
                q.append((temp,nh,ny,nx))
                result_day = max(temp, result_day)
            elif tomato_box[nh][ny][nx] != 1:
                if tomato_box[nh][ny][nx] > temp:
                    tomato_box[nh][ny][nx] = temp
                    q.append((temp,nh,ny,nx))
                    result_day = max(temp, result_day)
    return result_day

result = bfs(q)

flag = True
for h in range(1, H+1):
    for y in range(1, N+1):
        for x in range(1, M+1):
            if tomato_box[h][y][x] == 0:
                print(-1)
                flag= False
                break
        if not flag:
            break
    if not flag:
        break

if flag == True:
    print(result)

