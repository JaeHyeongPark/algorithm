import sys
N = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().strip()) for _ in range(N)]
# print(arr)

def sol(n, x, y):
    if n == 1:
        print(arr[x][y], end="")
        return

    #숫자 하나로만 이뤄지는지 체크
    check_param = True
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != arr[x][y]:
                check_param = False
                break

    if check_param == True:
        print(arr[x][y], end="")

    else:
        n //= 2
        print("(", end="")
        sol(n, x, y)
        sol(n, x, y+n)
        sol(n, x+n, y)
        sol(n, x+n, y+n)
        print(")", end="")

sol(N, 0, 0)