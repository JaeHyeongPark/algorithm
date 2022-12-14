#w[i][j] : i->j cost
#N, w 주어졌을 때, min cost

#비트연산자 출처: https://dojang.io/mod/page/view.php?id=2460

N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1 for _ in range(1 << N)] for _ in range(N)]

def dfs(row, visit, start, cnt):
    if cnt == N:
        return 0
    # 이미 해당 노선에 대해 최소비용이 계산되어 있다면 리턴!
    if visited[row][visit] != -1:
        return visited[row][visit]

    ret = 10000000
    for i in range(N):
        if visit & (1 << i) != 0 or city[row][i] == 0: 
        # 문법 : visit(이전에 방문했던 노드들)에 1<<i(1<<0이면 이진수 기준으로 1이므로 1번도시)
        # (1<<1이면 이진수 기준 10이므로 2번도시...)
        # 가 중복되거나, 현재(row)에서 i까지 가는 길이 막혀있다면,
        # 해당 노드를 이미 방문했거나 연결되어있지 않다면
            continue
        # 마지막 방문 도시인데 처음도시를 선택하지 않았거나, 마지막 방문 도시가 아닌데 처음도시를 선택한 경우
        if (cnt == N - 1 and i != start) or (cnt != N - 1 and i == start):
            continue

        ret = min(ret, dfs(i, visit | (1 << i), start, cnt + 1) + city[row][i])

    visited[row][visit] = ret

    return visited[row][visit]


print(dfs(0, 0, 0, 0))