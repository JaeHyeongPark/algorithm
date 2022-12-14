# 9:42 시작
import sys

K = int(sys.stdin.readline().strip()) # test case

def dfs(v, color):
    global dfs_flag
    visit_and_color[v] = color
    stack=[v]
    while stack:
        x = stack.pop()
        # print('x값은', x)
        for i in range(len(graph[x])):
            if visit_and_color[graph[x][i]] == visit_and_color[x]:
                dfs_flag = False
                break
            if visit_and_color[graph[x][i]] == False:
                stack.append(graph[x][i])
                visit_and_color[graph[x][i]] = -visit_and_color[x]

for _ in range(K):
    V, E = map(int, sys.stdin.readline().strip().split())
    visit_and_color = [ False for _ in range(V+1)]
    graph = [[] for _ in range(V+1)]
    flag = True
    dfs_flag = True

    for _ in range(E):
        i, j = map(int, sys.stdin.readline().strip().split())
        graph[i].append(j)
        graph[j].append(i)
    # print(graph)
    for m in range(1, V+1):
        if visit_and_color[m] == False:
            a = dfs(m,1)
            if dfs_flag == False:
                print('NO')
                flag = False
                break
    if flag != False:
        print('YES')