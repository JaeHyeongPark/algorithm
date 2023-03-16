import sys
N = int(sys.stdin.readline())
result = 0
chess_ground = [0] * N

#x 번째 행에 queen을 놓고 가능한지 확인
def isQueenPossible(x:int):
    for i in range(x):
        if chess_ground[i] == chess_ground[x] or abs(x-i) == abs(chess_ground[x] - chess_ground[i]):
            return False
    return True

# n 번째 queen 을 놓음
def countQueen(n:int):
    if n == N:
        global result
        result += 1
        return
    # 모든 column에 대해 다 놓아봄
    for i in range(N):
        chess_ground[n] = i
        if isQueenPossible(n):
            countQueen(n+1)

countQueen(0)
print(result)