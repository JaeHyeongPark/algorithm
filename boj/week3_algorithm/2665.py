import sys
from collections import deque

n = int(sys.stdin.readline().strip())
room = []
#out of index 이슈를 피하기 위해 padding 처리
room.append([False for _ in range(n+1)])
for _ in range(n):
    room.append([False]+list(map(int, sys.stdin.readline().strip())))
#방은 0이 검은방 1이 흰방
dx = [0 ,1, -1, 0]
dy = [1, 0, 0, -1]

black_room_count = [[float('INF') for _ in range(n+1)] for _ in range(n+1)]

def bfs(y, x):
    q = deque()
    q.append((0,y,x)) #지금 위치까지 오면서 만난 검은방 개수 중에 최소값 넘겨주기.
    while q:
        curr = q.popleft()
        count = curr[0]
        y = curr[1]
        x = curr[2]

        for i in range(2):
            ny = y + dy[i]
            nx = x + dx[i]
            blackcount = count
            if nx <1 or nx>n or ny<1 or ny>n:
                continue
            if room[ny][nx] == 0:
                blackcount = count + 1
            if blackcount < black_room_count[ny][nx]:
                black_room_count[ny][nx] = blackcount
                q.append((blackcount, ny, nx)) 
bfs(1,1)
print(black_room_count[n][n])