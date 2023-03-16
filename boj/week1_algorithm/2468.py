import sys
from collections import deque

N = int(sys.stdin.readline()) #2~100
heights = [[] for _ in range(N)] #1~100
for i in range(N):
    heights[i] = list(map(int, sys.stdin.readline().split(" ")))

maxHeight = max([max(heights[i]) for i in range(N)])

def check_safety(i:int,j:int,h:int):
    visited[i][j] = 1
    dir_x = [0, -1, 1, 0] #dx
    dir_y = [1, 0, 0, -1] #dy
    q = deque()
    q.append([i,j])

    while q:
        temp_point = q.popleft()
        curr_x = temp_point[0]  #x
        curr_y = temp_point[1]  #y

        for i in range(4):
            new_x = curr_x + dir_x[i]   #nx
            new_y = curr_y + dir_y[i]   #ny

            if new_x >= 0 and new_x <= N-1 and new_y >= 0 and new_y <= N-1 and heights[new_x][new_y] > h and visited[new_x][new_y]==0:
                q.append([new_x, new_y])
                visited[new_x][new_y] = 1

count_list = []

for h in range(0, maxHeight):
    count = 0
    visited = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and heights[i][j] > h:
                check_safety(i,j,h)
                count += 1
    count_list.append(count)

# print(count_list)
print(max(count_list))
