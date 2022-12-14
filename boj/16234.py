import sys
#N:1~50, 1<=L<=R<=100
N, L, R = list(map(int, sys.stdin.readline().strip().split()))
#matrix A
#elements are 0~100
A = []
for i in range(N):
    A.append(list(map(int, sys.stdin.readline().strip().split())))

# 나라 쭉 돌면서 인근 나라들이랑 인구차이 비교

# 2차원 배열(matrix), lower bound, upper bound가 input
def sol(mat:list, lb:int, ub:int):
    